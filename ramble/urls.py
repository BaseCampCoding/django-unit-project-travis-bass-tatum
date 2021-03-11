from django.urls import path
from .views import(
    UserListView, 
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit/',
        UserUpdateView.as_view(), name='user_edit'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/delete/',
        UserDeleteView.as_view(), name='user_delete'),
    path('', UserListView.as_view(), name='user_list'),
]
