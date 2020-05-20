from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from users.models import CustomUser
from django.db.models.functions import Concat
from django.db.models import Value

# Create your views here.
class Contactos(View):
    @method_decorator(login_required)
    def get(self, request):
        # Before getting here, must pass trough the login page

        # Get only data for showing (ignoring username, passwords, groups...)
        contactos_list = CustomUser.objects.values(
            'first_name',
            'last_name',
            'cargo',
            'curso',
            'email',
            'telemovel',
            'cc_num',
        )
        context = {
            'name': 'contactos',
            'contactos_list': contactos_list,
        }
        return render(request, 'contactos/contactos.html', context);
