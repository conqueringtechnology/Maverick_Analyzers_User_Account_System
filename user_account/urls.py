from django.urls import path
from user_account import views as user_views
from .views import password_reset_request, password_reset_set_password, ProfileView

app_name = 'user_account'

urlpatterns = [
    path('', user_views.home_view, name='home'),
    path('home/', user_views.home_view, name='home'),
    path('about/', user_views.about_view, name='about'),
    # Authentication
    path('login/', user_views.login_user_view, name='login'),
    path('logout/', user_views.logout_user_view, name='logout'),
    # Profile Page
    path('create_account/', user_views.create_account_view, name='create_account'),
    path('profile/', ProfileView.as_view(), name='profile_view'),
    path('profile_update/', user_views.profile_update, name='profile_update'),
    # Password Reset
    path('password_reset_request/', password_reset_request, name='password_reset_request'),
    path('password_reset_set_password/<uidb64>/<token>/', password_reset_set_password,
         name='password_reset_set_password'),
]
