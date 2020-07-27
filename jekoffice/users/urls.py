from django.urls import path
from . import views

urlpatterns = [
    path('editar_perfil/', views.EditarPerfil.as_view(), name='editar_perfil'),
]
