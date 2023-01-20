from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUser

class RegisterUserView(CreateView):
    form_class = RegisterUser
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')