from django import forms

class RegistroArticuloForm(forms.Form):
    Artículo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Artículo'}))
    Descripción = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Descripción'}))
    precio = forms.IntegerField()
    
class BusquedaForm(forms.Form):
    Artículo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Artículo'}))
    Descripción = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Descripción'}))
    