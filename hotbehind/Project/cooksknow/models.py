from django.db import models
from django.urls import reverse
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.db.models import Aggregate, Avg

from users.models import CustomUser

class Setting(models.Model):
    #Setting represents what environments a restaurant can have.  (ie: Dinner, Brunch, Fast-Food, Family, etc...)
    #Settings is a many to many field with Restaurants
    options = models.TextField(max_length=4)
    
    def __str__(self):
        return self.options

class Cuisine(models.Model):
    #Cuisines are a many to many field with Restaurants describing the cuisine types for a restaurant. 
    options = models.TextField(max_length=20)
    
    def __str__(self):
        return self.options
    
class Restaurant(models.Model):
    #the three specific fields for the Restaurant Model
    name = models.CharField(max_length=100, null=False, unique=False)
    location = models.CharField(max_length=500,blank=True)
    website = models.URLField(null=True,blank=True)
    hours = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='images/', default='default.jpg')

    #the relationship fields to other models.
    reviewers = models.ManyToManyField(CustomUser, related_name="Reviews", through="Review") #iterate through this to get the rating.  for x in reviewers x.rating
    cuisines = models.ManyToManyField(Cuisine, related_name="cuisines",blank=True)
    settings = models.ManyToManyField(Setting, related_name="settings",blank=True)
    
    #this property finds the average rating of the reviews for each restaurant.  It is given as a field in the API serializer.      
    @property
    def avg_rating(self):
        #for each restaurant, get all reviews of that restaurant.  Add the ratings up and divinde by the number of ratings to find the average rating. 
        return self.review_set.aggregate(Avg('rating'))['rating__avg']


    def get_absolute_url(self):
        return reverse('cooksknow:detail', args=(self.id,))

    def __str__(self):
        return self.name
    

class Review(models.Model):
    body = models.TextField(max_length=1000, blank=False,
                            unique=False, editable=True) #review text body

    #string representations of the integerfield rating selections. 
    RATING_CHOICES = (
        (1, 'Poor'),
        (2, 'Decent'),
        (3, 'Good'),
        (4, 'Great'),
        (5, 'Exceptional'),
    ) 

    rating = models.IntegerField(choices=RATING_CHOICES, blank=False, null=True) #used in the @property method avg_rating in Restaurant model
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #FK to users
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) #FK to Restaurant
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __repr__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('cooksknow:reviewdetail', args=(self.id,))
