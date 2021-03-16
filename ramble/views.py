from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, 
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from accounts.models import User
from .models import Post

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
    fields = ('username', 'email', 'hide_email',)
    template_name = 'user_edit.html'
    success_url = reverse_lazy('user_list')


class  UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body', 'author',)

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body',)
    template_name = 'post_edit.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def room(request, room_name):
    return render(request, 'chat/room.html',  {
        'room_name': room_name
    })

def room1(request):
    return render(request, 'chat/room1.html', {
        
    })

def room2(request):
    return render(request, 'chat/room2.html', {
        
    })

def room3(request):
    return render(request, 'chat/room3.html', {
        
    })

def room4(request):
    return render(request, 'chat/room4.html', {
        
    })

def room5(request):
    return render(request, 'chat/room5.html', {
        
    })

def chat(request):
    return render(request, 'chat/chat.html', {})