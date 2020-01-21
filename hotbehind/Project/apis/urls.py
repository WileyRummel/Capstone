from django.urls import path
from rest_framework.routers import DefaultRouter

from.views import ReviewViewSet, RestaurantViewSet, CuisineViewSet, SettingViewSet

router = DefaultRouter()
router.register('cuisines',CuisineViewSet, basename='cuisines')
router.register('settings',SettingViewSet, basename='settings')
router.register('restaurants',RestaurantViewSet, basename='restaurants')
router.register('reviews',ReviewViewSet, basename='reviews')

urlpatterns = router.urls
# path('cuisines',ListCuisine.as_view()),
# path('cuisines/<int:pk>/', DetailCuisine.as_view()),
# path('settings',ListSetting.as_view()),
# path('settings/<int:pk>/', DetailSetting.as_view()),
# path('restaurants',ListRestaurant.as_view()),
# path('restaurants/<int:pk>/', DetailRestaurant.as_view()),
# path('reviews',ListReview.as_view()),
# path('reviews/<int:pk>/', DetailReview.as_view()),
