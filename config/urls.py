"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static

import ramble.views
from ramble.views import (
    HomeView,
    SignUpView,)

from posts.views import(
    PostCreateView,
    PostListView,
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
    CommentCreateView,
)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('chat/', ramble.views.chat, name='chat'),
    path('profiles/', include("ramble.urls")),
    path('profiles/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('comment/', CommentCreateView.as_view(), name='comment' ),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('registration/', include('django.contrib.auth.urls')),
    path('chat/<str:room_name>/', ramble.views.room, name='room'),
    path('chat/public1/', ramble.views.room, name='public1'),
    path('chat/public2/', ramble.views.room, name='public2'), 
    path('chat/public3/', ramble.views.room, name='public3'), 
    path('chat/public4/', ramble.views.room, name='public4'), 
    path('chat/public5/', ramble.views.room, name = 'public5'),
    path('posts/', include('posts.urls')),
]
