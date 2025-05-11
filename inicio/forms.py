from django import forms

class RegistroArticuloForm(forms.Form):
    articulo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=20)
    precio = forms.IntegerField()
    
class BusquedaForm(forms.Form):
    articulo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Articulo'}))
    descripcion = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Descripcion'}))