from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from mensajeria.models import Mensaje
from django.views.generic.edit import CreateView
from mensajeria.forms import EnviarMensajeForm
from django.urls import reverse_lazy

# @login_required
# def enviar_mensaje(request):
#    return render(request, 'mensajeria/enviar_mensaje.html', {})
class EnviarMensaje(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = EnviarMensajeForm
    template_name = 'mensajeria/enviar_mensaje.html'
    success_url = reverse_lazy('mensajeria:listar_mensaje')
    
    def form_valid(self, form):
        form.instance.remitente = self.request.user
        return super().form_valid(form)


@login_required
def ver_mensaje(request, mensaje_id):
    mensaje = Mensaje.objects.get(id=mensaje_id)
    
    return render(request, 'mensajeria/ver_mensaje.html', {'mensaje': mensaje})

@login_required
def listar_mensaje(request):
    
    recibidos = Mensaje.objects.filter(destinatario=request.user)
    enviados = Mensaje.objects.filter(remitente=request.user)
    mensajes = recibidos | enviados
    mensajes = mensajes.order_by('-fecha_envio')  # Ordenar por fecha de envío
    return render(request, 'mensajeria/listar_mensaje.html', {'recibidos': recibidos, 'enviados': enviados, 'mensajes': mensajes})