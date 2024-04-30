from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user_account import views as user_views
from .views import password_reset_request, password_reset_set_password


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
    # path('profile/', user_views.profile_create_view, name='profile'),
    # Password Reset
    path('password_reset_request/', password_reset_request, name='password_reset_request'),
    path('password_reset_set_password/<uidb64>/<token>/', password_reset_set_password,
         name='password_reset_set_password'),
]

# Serve static files for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
