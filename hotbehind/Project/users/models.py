from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    approved = models.BooleanField(default=False) #default for users to not be approved.  Passing a quiz will toggle to True
    
    ROLE_CHOICES = ['FOH','BOH','CHEF','GM']
    role = models.CharField(max_length=4, null=True, choices=ROLE_CHOICES) #Default to null, lets user select BOH or FOH.  (BOH=True | FOH=False)


    # username = models.CharField(max_length=120, unique=True) #Usernames must be unique and length limiter
    # date_joined = models.DateTimeField(auto_now_add=True) #sign up date
    updated = models.DateTimeField(auto_now=True) #date & time for account changes

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username
