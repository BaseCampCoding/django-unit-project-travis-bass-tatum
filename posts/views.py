from django.views.generic import ListView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, 
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy

# Create your views here.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/post_new.html'
    fields = ('title', 'body',)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/post_list.html'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'body',)
    template_name = 'posts/post_edit.html'

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('post_list')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class CommentCreateView(CreateView):
    model = Comment
    fields = ['post', 'comment', 'author',]