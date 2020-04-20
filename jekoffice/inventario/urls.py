from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inventario.as_view(), name='inventario'),
    path('create/', views.ItemCreateView.as_view(), name='create_item'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update_item'),
]
