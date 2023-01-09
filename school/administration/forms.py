from django import forms

class CreateClassroomForm(forms.Form):
    name = forms.CharField(max_length=2, label='Nombre del aula', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    start_time = forms.TimeField(label='Hora de entrada', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
