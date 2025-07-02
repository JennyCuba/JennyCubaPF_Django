from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class RegistroDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        # help_texts = {'username': '', 'email': '', etc}
        help_texts = {
            key: ''
            for key in fields
        }
        
class EditarPerfil(UserChangeForm):
    email = forms.EmailField(required=False, label='Correo Electrónico')
    password = None
    
    first_name = forms.CharField(required=False, label='Nombre')
    last_name = forms.CharField(required=False, label='Apellido')
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        help_texts = {
            key: ''
            for key in fields
        }
