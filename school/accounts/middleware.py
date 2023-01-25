from ipware import get_client_ip
from django.http import HttpResponse
import requests

# Vamos a crear un middleware que verifique la ip del usuario y ver
# si lo dejamos pasar

"""
    Los middlewares reciben un parametro llamado get_response
"""

# Obtener ip del cliente

# 1. Vamos a crear un black list de IP's que no pueden entrar a nuestro proyecto

BLACK_LIST = ['172.18.0.1']


def is_valid_ip(get_response):
    """
        Esta funcion is_valid_ip va a retornar otra funcion
        ¿Porque? Porque necesitamos que exista una respuesta al cliente
        Pueden ser 2 tipos de respuestas:
        success: 201, 200
        error: 500, 404, 403, 401
    """

    # Esta funcion ya recibe un request
    
    def middleware(request):

        ip, is_routable = get_client_ip(request)

        response = get_response(request)

        response = requests.get(f"https://ipgeolocation.abstractapi.com/v1/?api_key=b5c4fdb157504078ba8b8f0ced826a35&ip_address={ip}")


        if ip in BLACK_LIST:
            return HttpResponse('Estas baneado :(')
      
        return response
    
    return middleware

# Version con clases


class IpValid:
    """
        __init__: sirve como constructor 
        __call__: se ejecuta antes de mostrar la vista
    """

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        ip, is_routable = get_client_ip(request)

        content = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=40213bf4125645b6b0ef263b4aeaf88f&ip_address=' + ip).json()

        if content['country'] == 'Peru':
            response = self.get_response(request)

            return response
        
        return HttpResponse('Es solo para Perú')

class Enter:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        response = self.get_response(request)

        return response




