from django import forms
from stock.models import MovimientoStock

class ActualizarStockForm(forms.ModelForm):
    
    class Meta:
        model = MovimientoStock
        fields = ['tipo']