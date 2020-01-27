from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('quiz/',) make a view and form for the quiz or do it all in JS?

]