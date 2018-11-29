from django import forms
from .models import Capacidad


class CapacidadForm(forms.ModelForm):

    class Meta:
        model = Capacidad
        fields = [
            'capacidadMax',
            'capacidadMin',
        ]
        labels = {
            'capacidadMax': 'Max. Capacidad',
            'capacidadMin': 'Min. Capacidad',
        }
        widgets = {
            'capacidadMax': forms.TextInput(attrs={'class':'form-control'}),
            'capacidadMin': forms.TextInput(attrs={'class':'form-control'}),
        }