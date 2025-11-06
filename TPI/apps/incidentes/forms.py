
from django import forms
from .models import Incidente # Asegúrate de que tu modelo Incidente esté aquí

class ReporteIncidenteForm(forms.ModelForm):
    """
    Formulario para el reporte rápido de un incidente.
    """
    class Meta:
        model = Incidente
        # Incluye solo los campos que el operario DEBE llenar
        fields = ['detalle', 'gravedad', 'latitud', 'longitud'] 
        
        # Opcional: Personaliza los labels de los campos
        labels = {
            'detalle': 'Descripción del Problema',
            'gravedad': 'Nivel de Gravedad',
        }