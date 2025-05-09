from django import forms

class RegistroArticuloForm(forms.Form):
    articulo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=20)
    precio = forms.IntegerField()
    
class RegistroForm(forms.Form):
    articulo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=20)
    precio = forms.IntegerField()