from django.urls import path 
# Django tiene un template de login preparado para el login
# Nos provee de la clase LoginView para poder mostrar el formulario de inicio de sesion
from django.contrib.auth.views import LoginView, logout_then_login
from . import views

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/register/', views.RegisterUserView.as_view(), name='register'),
    path('accounts/logout', logout_then_login, name='logout' ),
    path('test/', views.test_celery, name='celery')
]

"""
 LoginView
 va a buscar al archivo registration/login.html
 template_name = 'registration/login.html'
 Esta clase recibe 2 cosas username y password 
 Dentro de la clase va a verificar que el username y el password ingresado sea correctos
 
 Para que este funcione hay que seguir ciertas reglas:
 1: La url se debe llamar accounts/login (opcional)
 2: El template de login debe estar en la carpeta -> templates/registration/login.html
"""


