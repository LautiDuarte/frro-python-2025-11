
from django import forms
from .models import Incidente

class ReporteIncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ['detalle', 'gravedad', 'latitud', 'longitud'] 
        labels = {
            'detalle': 'Descripción del Problema',
            'gravedad': 'Nivel de Gravedad',
        }