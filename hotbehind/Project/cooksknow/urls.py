from django.urls import path
from . import views

app_name = 'cooksknow'

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name="RestaurantListView"),
    path('restaurant/<int:pk>/', views.RestaurantDetailView.as_view(), name='detail'),
    path ('create/', views.RestaurantCreateView.as_view(), name="new"),

]