from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm 



class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = User
	list_display = ['email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff']
	fieldsets = UserAdmin.fieldsets + ((None, {'fields':('is_active', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser' )}))
	add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields':('is_active', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser' )}))
	
	
admin.site.register(User, CustomUserAdmin)
