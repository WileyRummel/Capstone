from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Restaurant, Cuisine, Setting, Review

# Create your views here.
 
class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurants.html'

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant_detail.html'

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    template_name = 'restaurant_new.html'
    fields = ['name','location','website']

    def form_valid(self, form):
        return super().form_valid(form)
        

