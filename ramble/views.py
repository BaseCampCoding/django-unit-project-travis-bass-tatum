from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from accounts.models import User

# Create your views here.

class HomeView(ListView):
    model = User
    context_object_name = "users"
    template_name = "home.html"

class AccountListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

class AccountDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "signup.html"
