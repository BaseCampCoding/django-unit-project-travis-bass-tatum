from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from accounts.forms import RegistrationForm

def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenicated:
        return HttpResponse(f"You are already authenicated as {user.email}.")
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password')
            accounts = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("home")

        else:
            context['registration_form'] = form

    return render(request, 'accounts/register/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect("home")

def login_view(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated: 
        return redirect("home")

    destination = get_redirect_if_exists(request)

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                if destination:
                    return redirect(destination)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, "accounts/register/login.html", context)