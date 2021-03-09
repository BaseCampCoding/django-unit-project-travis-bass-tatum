from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from accounts.forms import RegisterForm

def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenicated:
        return HttpResponse(f"You are already authenicated as {user.email}.")
    context = {}
    if request.POST:
        form = RegisterForm(request.POST):
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("home")

        else:
            context['registration_form'] = form

    return render(request, 'accounts/signup.html', context)
