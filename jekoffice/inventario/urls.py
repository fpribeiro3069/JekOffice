from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inventario.as_view(), name='inventario'),
]
