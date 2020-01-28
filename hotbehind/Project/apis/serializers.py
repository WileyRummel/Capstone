from rest_framework import serializers
from cooksknow import models
from users.models import CustomUser

#You will come into an issue with it display the PJ for each model.  You will need to make a new model and serializer just to hold that.  Ask Brandon or Austen if you can't figure it out. 


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'options',
        )
        model = models.Cuisine

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'options',
        )
        model = models.Setting

class RestaurantSerializer(serializers.ModelSerializer):
    #these info subSerializers are to get a string representation of the respective models(source) instead of the PK.  ex: cuisines = American, not cuisines = 1
    setting_info = SettingSerializer(many=True, read_only=True,source='settings')
    cuisine_info = CuisineSerializer(many=True, read_only=True,source='cuisines')

    
    class Meta:
        fields = (
            'id',
            'name',
            'location',
            'hours',
            'website',
            'cuisines',
            'settings',
            'reviewers',
            'setting_info',
            'cuisine_info',
            'photo',
        )
        model = models.Restaurant


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username',
            'id',
            'role',
        )
        model = CustomUser

class ReviewSerializer(serializers.ModelSerializer):
    #these info subSerializers are to get a string representation of the respective models(source) instead of the PK.  ex: cuisines = American, not cuisines = 1

    # setting_info = SettingSerializer(many=True, read_only=True,source='settings')
    # cuisine_info = CuisineSerializer(many=True, read_only=True,source='cuisines')
    restaurant_info = RestaurantSerializer(many=False, read_only=True, source='restaurant')
    author_info = UsersSerializer(many=False, read_only=True, source="author")
    
    class Meta:
        fields = (
            'id',
            'author',
            'restaurant',
            'body',
            'rating',
            'created',
            'restaurant_info',
            'author_info'
        )
        model = models.Review

