from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import (
    CreateView, 
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from accounts.models import User

# Create your views here.

class HomeView(ListView):
    model = User
    context_object_name = "users"
    template_name = "home.html"

class  UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class  UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class  UserUpdateView(UpdateView):
    model = User
    template_name = 'user_edit.html'

class  UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
