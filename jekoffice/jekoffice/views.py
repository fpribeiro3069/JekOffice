from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# class Homepage(View):
#     @method_decorator(login_required)
#     def get(self, request):
#         # Before getting here, must pass trough the login page
#         response = redirect('login')
#         return response
