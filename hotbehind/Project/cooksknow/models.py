from django.db import models
from django.urls import reverse
from django.core.files import File
from django.core.files.storage import FileSystemStorage
# from django.db.models import DateTimeField

from users.models import CustomUser

class Setting(models.Model):
    
    options = models.TextField(max_length=4)
    
    def __str__(self):
        return self.options

class Cuisine(models.Model):
    
    options = models.TextField(max_length=10)
    
    def __str__(self):
        return self.options
    
fs = FileSystemStorage(location = '/media/photos')
class Restaurant(models.Model):
    #the three specific fields for the Restaurant Model
    name = models.CharField(max_length=100, null=False, unique=False)
    location = models.CharField(max_length=500,blank=True)
    website = models.URLField(null=True,blank=True)
    hours = models.TextField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='images', default='default.jpg')

    #the relationship fields to other models.

    reviewers = models.ManyToManyField(CustomUser, related_name="Reviews", through="Review") #iterate through this to get the rating.  for x in reviewers x.rating
    cuisines = models.ManyToManyField(Cuisine, related_name="cuisines",blank=True)
    settings = models.ManyToManyField(Setting, related_name="settings",blank=True)
    def get_absolute_url(self):
        return reverse('cooksknow:detail', args=(self.id,))

    def __str__(self):
        return self.name
    

class Review(models.Model):
    body = models.TextField(max_length=1000, blank=False,
                            unique=False, editable=True)

    RATING_CHOICES = (
        (1, 'Poor'),
        (2, 'Decent'),
        (3, 'Good'),
        (4, 'Great'),
        (5, 'Exceptional'),
    ) #this comes back as the string, but HTML display the number.  Research issue

    rating = models.IntegerField(choices=RATING_CHOICES, blank=False, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # cuisines = models.ManyToManyField(Cuisine, related_name="ReviewCuisines", blank=True)
    # settings = models.ManyToManyField(Setting, related_name="ReviewSettings", blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('cooksknow:reviewdetail', args=(self.id,))
