from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.contrib.auth import login, user_logged_out, get_user_model
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.views.generic import DetailView

from .forms import CreateAccountForm, ProfileForm, UserUpdateForm, CustomSetPasswordForm
from .models import Profile


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
        if create_account_form.is_valid():
            create_account_form.save()
            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('user_account:login')
    else:
        create_account_form = CreateAccountForm()

    context = {'create_account_form': create_account_form}
    return render(request, 'authentication/create_account.html', context)


# Login User
def login_user_view(request):
    login_form = AuthenticationForm()

    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            return redirect('user_account:home')

    context = {'login_form': login_form}
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


# Password Reset Feature
# Password Reset Form to send the reset password link to the user.
def password_reset_request(request):
    if request.method == 'POST':
        reset_form = PasswordResetForm(request.POST)
        if reset_form.is_valid():
            reset_form.save(
                request=request,
                from_email='info@maverickanalyzers.conqueringtechnology.com',
                email_template_name='password/password_reset_email_body.html',
                subject_template_name='password/password_reset_subject.txt',
            )
            messages.success(request, 'We have emailed you instructions for resetting your password, if an account exists with the email you entered. You will receive a reset link shortly.')
            return redirect('user_account:login')
    else:
        reset_form = PasswordResetForm()

    context = {'reset_form': reset_form}
    return render(request, 'password/password_reset_request.html', context)


# Set New Password Form
def password_reset_set_password(request, uidb64, token):
    custom_user_model = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = custom_user_model._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, custom_user_model.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            set_password_form = CustomSetPasswordForm(user, request.POST)
            if set_password_form.is_valid():
                set_password_form.save()
                messages.success(request, 'Your password has been successfully reset.')
                return redirect('user_account:login')
        else:
            set_password_form = CustomSetPasswordForm(user)

        context = {'set_password_form': set_password_form}
        return render(request, 'password/password_reset_set_password.html', context)
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return redirect('user_account:password_reset_request')


# Profile
# Profile View
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileView(DetailView):
    model = Profile
    template_name = 'profile/profile.html'

    # Retrieve logged in user data
    def get_object(self, queryset=None):
        return Profile.objects.get(custom_user=self.request.user)


# Profile & Custom User Update
@login_required(login_url='/login/')
def profile_update(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_form.is_valid():
            user_update_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('user_account:profile_view')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_update_form': user_update_form,
        'profile_form': profile_form
    }
    return render(request, 'profile/profile_update.html', context)
