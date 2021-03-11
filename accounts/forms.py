from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):


	class Meta(UserCreationForm):
		model = User
		fields = UserCreationForm.Meta.fields + ('email', 'username', 'password1', 'password2', )

	


class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = User
		fields = UserChangeForm.Meta.fields

	

# class CustomUserUpdateForm(UserUpdateForm):
    
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'profile_image', 'hide_email' )
