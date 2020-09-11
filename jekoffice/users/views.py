from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from phonenumber_field.modelfields import PhoneNumber
from django.conf import settings

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
            #'image_url': settings.MEDIA_URL + current_user.imagem.url,
            'user': current_user,
        }
        return render(request, 'users/editar_perfil.html', context)

    @method_decorator(login_required)
    def post(self, request):
        current_user = CustomUser.objects.get(pk=request.user.pk)
        form = CustomUserForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('editar_perfil')
        return redirect('inventario')
