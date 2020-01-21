from django.shortcuts import render
from rest_framework import viewsets

from cooksknow import models
from .serializers import RestaurantSerializer, ReviewSerializer, CuisineSerializer, SettingSerializer

#Using view sets for easy and verbose representation of Models through the API.  Allows basic CRUD and

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer


class CuisineViewSet(viewsets.ModelViewSet):
    queryset = models.Cuisine.objects.all()
    serializer_class = CuisineSerializer


class SettingViewSet(viewsets.ModelViewSet):
    queryset = models.Setting.objects.all()
    serializer_class = SettingSerializer
