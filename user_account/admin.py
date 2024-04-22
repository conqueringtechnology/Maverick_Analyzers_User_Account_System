from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile, AuthenticationLog


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'custom_user', 'player_bio')


class AuthenticationLogAdmin(admin.ModelAdmin):
    list_display = ('custom_user', 'login_timestamp', 'logout_timestamp')


"""Model Register"""
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AuthenticationLog, AuthenticationLogAdmin)
