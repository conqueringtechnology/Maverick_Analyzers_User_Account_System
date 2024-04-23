import random
import string

from django.contrib.auth import user_logged_out, user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import CustomUser, Profile, AuthenticationLog


# Function to generate random display name
def random_display_name():
    result_display_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return f"User_{result_display_name}"


# Create a Profile when the user creates account
@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        display_name = random_display_name()
        while Profile.objects.filter(display_name=display_name).exists():
            display_name = random_display_name()
        Profile.objects.create(custom_user=instance, display_name=display_name)


# Save the Profile everytime the User is saved
@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()


# Login Timestamp when user logs in
@receiver(user_logged_in)
def user_log_login(sender, request, user, **kwargs):
    AuthenticationLog.objects.create(custom_user=user, login_timestamp=timezone.now())


# Login Timestamp when user logs in
@receiver(user_logged_out)
def user_log_logout(sender, request, user, **kwargs):
    auth_log = AuthenticationLog.objects.filter(custom_user=user).last()
    if auth_log:
        auth_log.logout_timestamp = timezone.now()
        auth_log.save()
    else:
        AuthenticationLog.objects.create(custom_user=user, logout_timestamp=timezone.now())