from django.db import models
from django.urls import reverse

from users.models import CustomUser

class Setting(models.Model):
    
    options = models.TextField(max_length=4)

class Cuisine(models.Model):
    
    options = models.TextField(max_length=10)
    def __str__(self):
        return self.options
    

class Restaurant(models.Model):
    #the three specific fields for the Restaurant Model
    name = models.CharField(max_length=100, null=False, unique=False)
    location = models.CharField(max_length=500,blank=True)
    website = models.URLField(null=True,blank=True)

    #the relationship fields to other models.

    reviewers = models.ManyToManyField(CustomUser, related_name="Reviews", through="Review")
    cuisines = models.ManyToManyField(Cuisine, related_name="cuisines",blank=True)
    settings = models.ManyToManyField(Setting, related_name="settings",blank=True)

    #not sure how to incorporate ratings from reviews
    # rating = models.ForeignKey(Review, null=True, on_delete=models.CASCADE)
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
    )

    rating = models.IntegerField(choices=RATING_CHOICES, blank=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurantrev = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
