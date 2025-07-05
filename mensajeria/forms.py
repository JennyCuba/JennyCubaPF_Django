from django.forms import ModelForm
from mensajeria.models import Mensaje
from datetime import datetime

class EnviarMensajeForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']
        

