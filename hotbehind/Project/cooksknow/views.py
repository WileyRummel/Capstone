from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from datetime import datetime

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
    fields = ['name','location','website', 'cuisines','settings']

    def form_valid(self, form):
        return super().form_valid(form)

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review_new.html'
    fields = ['author','restaurant','body','rating']
    
    def form_valid(self,form):
        return super().form_valid(form)
    
class ReviewDetailView(DetailView):
    model: Review
    template_name = 'review_detail.html'


    def get_queryset(self):
        return Review.objects.order_by('-created')
        