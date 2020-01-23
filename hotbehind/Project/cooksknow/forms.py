from .models import Restaurant, Cuisine, Setting, Review
from django.db import models
from django.forms import ModelForm

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name','photo','location','website','cuisines','settings','reviewers']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['restaurant','rating','body']
