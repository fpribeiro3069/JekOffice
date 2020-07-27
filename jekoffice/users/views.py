from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import CustomUser
from .forms import CustomUserForm

# Create your views here.

class EditarPerfil(View):
    @method_decorator(login_required)
    def get(self, request):
        current_user = CustomUser.objects.get(pk=request.user.pk)
        form = CustomUserForm(instance=current_user)

        context = {
            'form': form,
        }
        return render(request, 'users/editar_perfil.html', context)

    @method_decorator(login_required)
    def post(self, request):

        pass
