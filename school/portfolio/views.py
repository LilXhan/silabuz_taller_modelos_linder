from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Portfolio(TemplateView):
    template_name = 'portfolio.html'

class Ticket(TemplateView):
    template_name = 'ticket.html'