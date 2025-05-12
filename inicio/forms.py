from django import forms

class BaseForm(forms.Form):
    Artículo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Artículo'}))
    Descripción = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Descripción'}))
    Precio = forms.IntegerField()
    
class CrearForm(BaseForm):
    pass

class EditarForm(BaseForm):
    pass
    
class BusquedaForm(forms.Form):
    Artículo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Artículo'}))
    Descripción = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Descripción'}))
    