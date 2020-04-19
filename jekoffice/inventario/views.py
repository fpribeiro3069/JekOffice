from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Item

# Create your views here.
class Inventario(View):
    @method_decorator(login_required)
    def get(self, request):
        # Before getting here, must pass trough the login page
        inventario_list = Item.objects.all()
        context = {
            'inventario_list': inventario_list,
        }
        return render(request, 'inventario/inventario.html', context);
