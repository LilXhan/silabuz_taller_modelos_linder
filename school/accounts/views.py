from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView
from .tasks import sum

from .forms import RegisterUser

def test_celery(request):
    for x in range(1, 50):
        sum.delay(x + 2, x + 3)

    return HttpResponse('Usando celery...')

class RegisterUserView(CreateView):
    form_class = RegisterUser
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')