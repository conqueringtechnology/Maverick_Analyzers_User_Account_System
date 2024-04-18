from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from user_account.forms import CreateAccountForm
from user_account.models import Profile


# Home View
def home_view(request):
    return render(request, 'home.html')


# About View
def about_view(request):
    return render(request, 'about.html')


# Create User Account
def create_account_view(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('user_account:login')
    else:
        form = CreateAccountForm()

    context = {'form': form}
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
