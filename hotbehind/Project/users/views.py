from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# class QuizView(DetailView):
#     form_class = QuizForm
#     success_url = reverse_lazy('home')
#     template_name = 'quiz.html'

# class AddQuizView(CreateView):
#     form_class = AddQuizForm
#     success_url = reverse_lazy('home')
#     template_name = 'quiz_new.html'