from django.urls import path
from . import views

urlpatterns = [
    path('', views.Contactos.as_view(), name='contactos'),
]
