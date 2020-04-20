from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Item
from .forms import ItemForm

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView

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


class ItemCreateView(BSModalCreateView):
    template_name = 'inventario/create_item.html'
    form_class = ItemForm
    success_message = 'Sucesso: Item foi criado!'
    success_url = reverse_lazy('inventario')

class ItemUpdateView(BSModalUpdateView):
    model = Item
    template_name = 'inventario/update_item.html'
    form_class = ItemForm
    success_message = 'Success: Item foi atualizado!'
    success_url = reverse_lazy('inventario')
