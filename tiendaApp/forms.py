# En tu_app/forms.py
from django import forms

class CompraForm(forms.Form):
    nombre = forms.CharField(max_length=64, label="Nombre")
    direccion = forms.CharField(max_length=128, label="Dirección")
    telefono = forms.CharField(max_length=20, label="Teléfono")
    correo_electronico = forms.EmailField(label="Correo Electrónico")
