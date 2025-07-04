from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from django.contrib.auth.views import LogoutView, PasswordChangeView
from usuarios.forms import RegistroDeUsuario, EditarPerfil, CambiarContraseñaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from usuarios.models import InfoUsuario

def login(request):
    
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            
            django_login(request, usuario)
            
            InfoUsuario.objects.get_or_create(user=usuario)
            
            return redirect('inicio:inicio')
    
    return render (request, 'usuarios/iniciar_sesion.html', {'form': form})

class CerrarSesion(LoginRequiredMixin, LogoutView):
    template_name = 'usuarios/cerrar_sesion.html'
    
def registro(request):
    
    formulario = RegistroDeUsuario()
    
    if request.method == 'POST':
        formulario = RegistroDeUsuario()
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:iniciar_sesion')
       
    return render(request, 'usuarios/registro.html', {'form': formulario})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})
    
@login_required
def editar_perfil(request):
    
    info_usuario = request.user.infousuario
    formulario = EditarPerfil (initial={'avatar': info_usuario.avatar}, instance=request.user)
    
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance =request.user)
        
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar'):
                info_usuario.avatar = formulario.cleaned_data.get('avatar')
            info_usuario.save()
            formulario.save()
            return redirect('usuarios:perfil')
                
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})

class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    form_class = CambiarContraseñaForm
    template_name = 'usuarios/cambiar_contraseña.html'
    success_url = reverse_lazy('usuarios:perfil')
