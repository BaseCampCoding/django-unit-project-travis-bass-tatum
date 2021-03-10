from django.shortcuts import render
from django.views.generic import ListView, DetailView
from accounts.models import Account

# Create your views here.

class AccountListView(ListView):
    model = Account
    template_name = 'user_list.html'
    context_object_name = 'users'

class AccountDetailView(DetailView):
    model = Account
    template_name = 'user_detail.html'