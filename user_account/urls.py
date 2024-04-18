from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user_account import views as user_views

app_name = 'user_account'

urlpatterns = [
    path('', user_views.home_view, name='home'),
    path('home/', user_views.home_view, name='home'),
    path('about/', user_views.about_view, name='about'),
    path('create_account/', user_views.create_account_view, name='create_account'),
    # Authentication
    path('login/', user_views.login_user_view, name='login'),
    path('logout/', user_views.logout_user_view, name='logout'),
    # Profile Page
    # path('profile/', user_views.profile_create_view, name='profile'),
]

# Serve static files for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
