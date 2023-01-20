
# Vamos a crear un form para poder registrar usuarios

from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Por defecto django tiene un form con los siguientes campos

"""
username
email
password1
password2

En el formulario tenemos una seccion para confirmar que ambos password son iguales

Ahora si queremos aumentar mas campos al registro podemos hacer un customform y heredar de la
clase UserCreationForm
"""

class RegisterUser(UserCreationForm):
    
    email = forms.EmailField(required=True)

    class Meta:
        # Vamos a indicar que este formulario pertenece a un modelo
        model = User 
        # Luego podemos definir que campos seran los que mostremos usando el atributo fields
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

        # Vamos a sobreescribir el metodo save()
        # Para crear un usuario el usa el metodo save()

    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)

        # aumentar el email
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user