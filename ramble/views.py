from django.shortcuts import render
from django.views.generic import ListView, DetailView
from accounts.models import User

# Create your views here.

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'