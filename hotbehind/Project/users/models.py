from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    approved = models.BooleanField(default=False) #default for users to not be approved.  Passing a quiz will toggle to True
    
    ROLE_CHOICES = [
        ('FOH','Front of house'),
        ('BOH','Back of house'),
        ('CHEF','Chef'),
        ('GM','General Manager')
        ]
    role = models.CharField(max_length=4, null=True, choices=ROLE_CHOICES) #Default to null, lets user select BOH or FOH.  (BOH=True | FOH=False)


    # username = models.CharField(max_length=120, unique=True) #Usernames must be unique and length limiter
    # date_joined = models.DateTimeField(auto_now_add=True) #sign up date
    updated = models.DateTimeField(auto_now=True) #date & time for account changes

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username


#maybe the models for a quiz to be built and django and deployed with django class based forms
# class Quiz(models.Model):
#     name = models.CharField(max_length=1000)

# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     label = models.CharField(max_length=1000)
#     # answer = models.ManyToManyField(Answer)
#     def __str__(self):
#         return self.label

# class Answer(models.Model):
#     question = models.ManyToManyField(Question, on_delete=models.CASCADE)
#     text = models.CharField(max_length=1000)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return self.text