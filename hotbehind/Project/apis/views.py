#build in django and DRF stuff
# from django.response import response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework import authentication, permissions, authtoken
from rest_framework import filters

#local classes, models, etc.
from users.models import CustomUser
from cooksknow import models
from .permissions import IsAuthorOrReadOnly, IsApproved, IsAuthor, IsApprovedOrReadOnly
from .serializers import RestaurantSerializer, ReviewSerializer, CuisineSerializer, SettingSerializer

#Using view sets for easy and verbose representation of Models through the API.  Allows basic CRUD and

class RestaurantViewSet(viewsets.ModelViewSet):
    #giving permission only to logged in users
    permission_classes = (IsAuthorOrReadOnly, IsApprovedOrReadOnly)

    #getting all the database objects from data models and serializers
    queryset = models.Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['name','cuisines__options','settings__options','location']

class ReviewViewSet(viewsets.ModelViewSet):
    #giving permission only to logged in users

    permission_classes = (IsAuthorOrReadOnly,IsApprovedOrReadOnly)

    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['restaurant__name','rating','created','body']


class CuisineViewSet(viewsets.ModelViewSet):
    #giving permission only to logged in users
    permission_classes = (IsApprovedOrReadOnly, IsAuthorOrReadOnly)

    queryset = models.Cuisine.objects.all()
    serializer_class = CuisineSerializer


class SettingViewSet(viewsets.ModelViewSet):
    #giving permission only to logged in users
    permission_classes = (IsApprovedOrReadOnly, IsAuthorOrReadOnly)

    queryset = models.Setting.objects.all()
    serializer_class = SettingSerializer


'''Setting up an API VIEW:
- Request passed to the handler methods will be REST frameworks REQUEST instance, not Djangoe's HTTPREQUEST instances.  
- Handler methods may return REST frameworks RESPONSE instead of Djangoes HTTPRESPONSE. The view will manage conent negotiation and setting the correst renderer on the response
- Any APIException exceptions will be caught and mediated into appropriate responses. 
- Incoming requests will be authenticated and appropriate permissions and/or throttle checks will be run before dispatching the request to the handler method.  
'''
class UserApprovalSystem(APIView):
    '''This will be called after a user passes the quiz.  It will change CustumUser.approved from default=False to True. This gives them permission to make posts.'''
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def approval(self, request):
        """ psuedo code.  
        If user is logged in, go on (should be inherit from above):
        If user passes the quiz send this view:
        return self.user.approved = True """ 
        request.user.approved = True
        return "Success Url?"
