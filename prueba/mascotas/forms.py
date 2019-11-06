from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Producto
from django import forms
from .models import Ventas

class UsuarioForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
        }

class VentasForm(forms.ModelForm):
    
    class Meta:
        model = Ventas
        fields = [
            'rut',
            'nombre',
            'apellidos',
            'telefono',
            'email',
            'domicilio',
            'stock',
            'marca',
        ]
        labels = {
            'rut': 'RUT',
            'nombre': 'NOMBRE',
            'apellidos': 'APELLIDOS',
            'email': 'EMAIL',
            'domicilio' : 'DOMICILIO',
            'stock' : 'STOCK',
            'marca' : 'MARCA'
        }

        widgets = {
            'rut' :forms.TextInput(attrs={'class':'form-control'}),
            'nombre' :forms.TextInput(attrs={'class':'form-control'}),
            'apellidos' :forms.TextInput(attrs={'class':'form-control'}),
            'email' :forms.TextInput(attrs={'class':'form-control'}),
            'domicilio' :forms.TextInput(attrs={'class':'form-control'}),
            'stock' :forms.TextInput(attrs={'class':'form-control'}),
            'marca' :forms.Textarea(attrs={'class':'form-control'}),
        }