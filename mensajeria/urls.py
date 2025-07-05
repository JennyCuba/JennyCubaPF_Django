from django.urls import path
from mensajeria import views

app_name = 'mensajeria'

urlpatterns = [
    path('enviar_mensaje/', views.EnviarMensaje.as_view(), name='enviar_mensaje'),
    path('listar_mensaje/', views.listar_mensaje, name='listar_mensaje'),
    path('<int:mensaje_id>/', views.ver_mensaje, name='ver_mensaje'),
        
]

