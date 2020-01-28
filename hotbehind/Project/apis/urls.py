from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.request import Request

# CurrentUserView
from.views import ReviewViewSet, RestaurantViewSet, CuisineViewSet, SettingViewSet, UsersViewSet, CurrentUserView

router = DefaultRouter()
router.register('cuisines',CuisineViewSet, basename='cuisines')
router.register('settings',SettingViewSet, basename='settings')
router.register('restaurants',RestaurantViewSet, basename='restaurants')
router.register('reviews',ReviewViewSet, basename='reviews')
router.register('users', UsersViewSet, basename='users') 

# router.register('users/me',UsersViewSet.get_current(Request), basename="me") #trying to make a url for the users method


# router.register('currentuser', CurrentUserView, basename='currentuser')

urlpatterns =  [path('currentuser', CurrentUserView.as_view())] + router.urls



# path('cuisines',ListCuisine.as_view()),
# path('cuisines/<int:pk>/', DetailCuisine.as_view()),
# path('settings',ListSetting.as_view()),
# path('settings/<int:pk>/', DetailSetting.as_view()),
# path('restaurants',ListRestaurant.as_view()),
# path('restaurants/<int:pk>/', DetailRestaurant.as_view()),
# path('reviews',ListReview.as_view()),
# path('reviews/<int:pk>/', DetailReview.as_view()),
