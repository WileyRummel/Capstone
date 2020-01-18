from django.db import models

from users.models import CustomUser


# Create your models here.

class Review(models.Model):
    body = models.TextField(max_length=1000, null=False,
                            unique=False, editable=True)

    RATING_CHOICES = [
        (1, 'Poor'),
        (2, 'Decent'),
        (3, 'Good'),
        (4, 'Great'),
        (5, 'Exceptional'),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Restaurant(models.Model):
    reviewers = models.ManyToManyField(CustomUser, related_name="Reviews", through="Review")
    rating = models.ForeignKey(Review, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, unique=False)
    location = models.CharField(max_length=500, null=False)
    website = models.URLField(null=True)


    # cuisine = models.ManyToManyField(Cuisine)
    # setting = models.ManyToManyField(Setting)



class Setting(models.Model):
    
    options = models.TextField(max_length=4)
    pass


class Cuisine(models.Model):
    

    options = models.TextField(max_length=10)
    pass