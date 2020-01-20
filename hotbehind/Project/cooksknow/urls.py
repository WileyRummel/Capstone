from django.urls import path
from . import views

app_name = 'cooksknow'

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name="RestaurantListView"),
    path('<int:pk>/', views.RestaurantDetailView.as_view(), name='detail'),
    path('create/', views.RestaurantCreateView.as_view(), name="new"),
    path('review/', views.ReviewCreateView.as_view(), name="makereview"),
    path('review/<int:pk>/', views.ReviewDetailView.as_view(), name="reviewdetail")

]