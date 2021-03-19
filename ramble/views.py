from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.conf import settings
from django.views.generic.edit import (
    CreateView, 
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from accounts.models import User
from django.contrib.auth import get_user_model

# Create your views here.

class HomeView(ListView):
    model = User
    context_object_name = "users"
    template_name = "home.html"

class  UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class  UserDetailView(DetailView):
    model = get_user_model()
 

class  UserUpdateView(UpdateView):
    model = User
    fields = ('username', 'email', 'hide_email',)
    template_name = 'user_edit.html'
    success_url = reverse_lazy('user_list')


class  UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def room(request, room_name):

    return render(request, 'chat/room.html',  {
        'room_name': room_name
    })


def chat(request):
    return render(request, 'chat/chat.html', {})