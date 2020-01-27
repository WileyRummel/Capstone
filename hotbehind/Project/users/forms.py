from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        # fields = ('username', 'email','approved', 'role')
        fields = UserCreationForm.Meta.fields + ('approved','role')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # fields = ('username','email','approved', 'role')
        fields = UserCreationForm.Meta.fields + ('approved','role')

# class QuizForm():
#     class Meta:
#         model = Quiz
#         fields = ('question', 'answer')

# class AddQuizForm():
#     class Meta:
#         model = Quiz
#         fields = ('question','answer')