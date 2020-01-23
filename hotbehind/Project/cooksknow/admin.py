from django.contrib import admin
from .forms import RestaurantForm
from django.forms import ModelForm
from .models import Restaurant, Review, Setting, Cuisine

# Register your models here.

class CooksKnowAdmin():
    add_form = RestaurantForm
    form = ModelForm
    model = Restaurant
    list_display = []

admin.site.register([Restaurant, Review, Setting, Cuisine]) 