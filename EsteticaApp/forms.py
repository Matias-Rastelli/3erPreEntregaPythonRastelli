from django import forms
from .models import Turno

class ClientesForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.CharField()


class MasajesForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.DecimalField()
    duracion = forms.DurationField()


# class TurnosForm(forms.Form):
#     fecha = forms.DateField()
#     hora = forms.TimeField()
#     cliente = forms.CharField()
#     masaje = forms.CharField()


class TurnosForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['fecha', 'hora', 'cliente', 'masaje']