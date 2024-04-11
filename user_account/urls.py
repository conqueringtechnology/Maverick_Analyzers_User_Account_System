from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user_account import views as user_views

app_name = 'user_account'

urlpatterns = [
    path('', user_views.home, name='home'),
    path('home/', user_views.home, name='home'),
    path('about/', user_views.about, name='about'),
]

# Serve static files for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
