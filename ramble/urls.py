from django.urls import path
from .views import(
    AccountListView, 
    AccountDetailView,
)

urlpatterns = [
    path('', AccountListView.as_view(), name='user_list'),
    path('user/<int:pk>/', AccountDetailView.as_view(), name='user_detail'),
]
