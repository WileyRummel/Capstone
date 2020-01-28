#build in django and DRF stuff
# from django.http import response, request
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework import authentication, permissions, authtoken
from rest_framework import filters
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt # for csrf_exempt
from django.utils.decorators import method_decorator # for csrf_exempt

#local classes, models, etc.
from users.models import CustomUser
from cooksknow import models
from .permissions import IsAuthorOrReadOnly, IsApproved, IsAuthor, IsApprovedOrReadOnly
from .serializers import RestaurantSerializer, ReviewSerializer, CuisineSerializer, SettingSerializer, UsersSerializer

#Using view sets for easy and verbose representation of Models through the API.  Allows basic CRUD and
@method_decorator(csrf_exempt, name='dispatch')
class RestaurantViewSet(viewsets.ModelViewSet):
    #giving permission only to logged in users
    permission_classes = (IsAuthorOrReadOnly, IsApprovedOrReadOnly)

    #getting all the database objects from data models and serializers
    queryset = models.Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['name','cuisines__options','settings__options','location']


@method_decorator(csrf_exempt, name='dispatch')
class ReviewViewSet(viewsets.ModelViewSet):
    #giving permission only to logged in users

    permission_classes = (IsAuthorOrReadOnly,IsApprovedOrReadOnly)

    queryset = models.Review.objects.all().order_by('-created')
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


class UsersViewSet(viewsets.ModelViewSet):
    # need to build an admin permission class in order to only let admin see users API?  But then would review ssystem work?
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer

    

class CurrentUserView(APIView):
    def get(self, request):
        
        serializer = UsersSerializer(request.user)
        return Response(serializer.data)

   
'''Setting up an API VIEW:
- Request passed to the handler methods will be REST frameworks REQUEST instance, not Djangoe's HTTPREQUEST instances.  
- Handler methods may return REST frameworks RESPONSE instead of Djangoes HTTPRESPONSE. The view will manage conent negotiation and setting the correst renderer on the response
- Any APIException exceptions will be caught and mediated into appropriate responses. 
- Incoming requests will be authenticated and appropriate permissions and/or throttle checks will be run before dispatching the request to the handler method.  
'''
# class UserApprovalSystem(APIView):
#     '''This will be called after a user passes the quiz.  It will change CustumUser.approved from default=False to True. This gives them permission to make posts.'''
    
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = (permissions.IsAuthenticated,)
    
#     def approval(self, request):
#         """ psuedo code.  
#         If user is logged in, go on (should be inherit from above):
#         If user passes the quiz send this view:
#         return self.user.approved = True """ 
#         request.user.approved = True
#         return "Success Url?"
 # def retrieve(self, request: Request, *args, **kwargs):
    #     """
    #     If provided 'pk' is "me" then return the current user.
    #     """
    #     if kwargs.get('pk') == 'me':
    #         return Response(self.get_serializer(request.user).data)
    #     return super().retrieve(request, args, kwargs)
    # @classmethod
    # def get_current(self, Request):
    #     user = self.request.users
    #     print(user)
    #     return user



    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     if pk == "current":
    #         return self.request.user
    #     return super(UsersViewSet, self).get_object()


# @api_view(['GET'])
# def current_user(request):

#     serializer = UsersSerializer(request.user)
#     return response(serializer.data)
