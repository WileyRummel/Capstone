from django.shortcuts import render
from rest_framework import viewsets, permissions
from .permissions import IsAuthorOrReadOnly, IsApproved, IsAuthor

from cooksknow import models
from .serializers import RestaurantSerializer, ReviewSerializer, CuisineSerializer, SettingSerializer

#Using view sets for easy and verbose representation of Models through the API.  Allows basic CRUD and

class RestaurantViewSet(viewsets.ModelViewSet):
    #giving permission only to logged in users
    permission_classes = (IsAuthorOrReadOnly, IsApproved)

    #getting all the database objects from data models and serializers
    queryset = models.Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    #giving permission only to logged in users

    permission_classes = (IsAuthorOrReadOnly,IsApproved)

    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer


class CuisineViewSet(viewsets.ModelViewSet):
    #giving permission only to logged in users

    permission_classes = (IsAuthor, IsApproved, IsAuthorOrReadOnly)

    queryset = models.Cuisine.objects.all()
    serializer_class = CuisineSerializer


class SettingViewSet(viewsets.ModelViewSet):
    #giving permission only to logged in users
    permission_classes = (IsAuthor, IsApproved, IsAuthorOrReadOnly)

    queryset = models.Setting.objects.all()
    serializer_class = SettingSerializer
