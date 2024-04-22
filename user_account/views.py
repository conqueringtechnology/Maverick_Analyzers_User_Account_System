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
    error_message = None

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_account:home')
            else:
                error_message = 'Invalid username or password'
    else:
        login_form = LoginForm()

    context = {'login_form': login_form, 'error_message': error_message}
    return render(request, 'authentication/login.html', context)


# Logout User
def logout_user_view(request):
    if request.session.session_key:
        # Dispatch the built-in Django signal 'user_logged_out' to notify other parts of the application
        # that the user has been logged out.
        user_logged_out.send(sender=request.__class__, request=request, user=request.user)
        # Delete the session
        request.session.flush()
        # logs out the user by removing the authentication status from the current request.
        request.user = AnonymousUser()

    return redirect('user_account:login')