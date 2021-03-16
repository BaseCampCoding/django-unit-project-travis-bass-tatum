from django.urls import path
from .views import(
    UserListView, 
    UserUpdateView,
    UserDetailView,
    UserDeleteView,
    PostListView,
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
    PostCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
        UserUpdateView.as_view(), name='user_edit'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/delete/',
        UserDeleteView.as_view(), name='user_delete'),
    path('users/', UserListView.as_view(), name='user_list'),

    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/',
        PostDeleteView.as_view(), name='post_delete'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('', PostListView.as_view(), name='post_list'),
]
