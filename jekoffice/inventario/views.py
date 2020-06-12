from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Item
from .forms import ItemForm

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView

# Create your views here.
class Inventario(View):
    @method_decorator(login_required)
    def get(self, request):
        # Before getting here, must pass trough the login page
        inventario_list = Item.objects.all()

        page_number = request.GET.get('page', 1)
        paginate_result = self.do_paginate(inventario_list, page_number)
        inventario_list = paginate_result[0]
        paginator = paginate_result[1]
        base_url = '/inventario/?'

        context = {
            'name': 'inventario',
            'inventario_list': inventario_list,
            'paginator': paginator,
            'base_url': base_url,
        }
        return render(request, 'inventario/inventario.html', context);

    # Função auxiliar de paginação dos items
    def do_paginate(self, item_list, page_number):
        ret_data_list = item_list

        # Tem que ser dinâmico de acordo com a página
        results_per_page = 10

        paginator = Paginator(item_list, results_per_page)

        try:
        # get data list for the specified page_number.
            ret_data_list = paginator.page(page_number)
        except EmptyPage:
            # get the lat page data if the page_number is bigger than last page number.
            ret_data_list = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            # if the page_number is not an integer then return the first page data.
            ret_data_list = paginator.page(1)
        return [ret_data_list, paginator]


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
