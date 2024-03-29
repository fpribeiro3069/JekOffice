"""jekoffice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomAuthForm

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='inventario', permanent=False)),
    path('login/',  auth_views.LoginView.as_view(authentication_form=CustomAuthForm), name='login'),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')),
    path('contactos/', include('contactos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
