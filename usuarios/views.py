from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as django_login
from django.contrib.auth.views import LogoutView
from usuarios.forms import RegistroDeUsuario

def login(request):
    
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            
            django_login(request, usuario)
            return redirect('inicio:inicio')
    
    return render (request, 'usuarios/iniciar_sesion.html', {'form': form})

class CerrarSesion(LogoutView):
    template_name = 'usuarios/cerrar_sesion.html'
    
def registro(request):
    
    formulario = RegistroDeUsuario()
    
    if request.method == 'POST':
        formulario = RegistroDeUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:iniciar_sesion')
       
    return render(request, 'usuarios/registro.html', {'form': formulario})