from django.urls import path
from .views import(
    UserListView, 
    UserUpdateView,
    UserDetailView,
    UserDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit/',
        UserUpdateView.as_view(), name='user_edit'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/delete/',
        UserDeleteView.as_view(), name='user_delete'),
    path('users/', UserListView.as_view(), name='user_list'),
]
