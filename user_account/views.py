from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CreateAccountForm



# Home View
def home_view(request):
    return render(request, 'home.html')


# About View
def about_view(request):
    return render(request, 'about.html')


# Create User Account
def create_account_view(request):
    if request.method == 'POST':
        create_account_form = CreateAccountForm(request.POST)
        if create_account_form .is_valid():
            create_account_form.save()
            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('user_account:login')
    else:
        create_account_form = CreateAccountForm()

    context = {'create_account_form': create_account_form}
    return render(request, 'authentication/create_account.html', context)


# Login User
def login_user_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('user_account:home')

    context = {'form': form}
    return render(request, 'authentication/login.html', context)


# Logout User
def logout_user_view(request):
    logout(request)
    return redirect('user_account:login')
