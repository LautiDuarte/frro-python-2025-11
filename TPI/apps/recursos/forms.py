from django import forms
from .models import Recurso

class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['tipo_recurso']
        widgets = {
            'tipo_recurso': forms.Select(attrs={'class': 'border p-2 rounded w-full'}),
        }
