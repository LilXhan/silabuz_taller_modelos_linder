from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.Portfolio.as_view(), name='portfolio'),
    path('ticket/', views.Ticket.as_view(), name='ticket')
]