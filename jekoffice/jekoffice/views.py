from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Homepage(View):
    @method_decorator(login_required)
    def get(self, request):
        # Before getting here, must pass trough the login page
        context = {
            'message': "Homepage get: This is a message from the server",
        }
        return render(request, 'homepage.html', context);
