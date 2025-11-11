from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario 
from apps.recursos.models import Institucion

class CustomUserCreationForm(UserCreationForm):
    
    # Definimos el campo de institución aquí
    institucion_asignada = forms.ModelChoiceField(
        queryset=Institucion.objects.all(),
        required=False,
        label="Institución de Afiliación",
    )
    
    # Definimos el campo de rol aquí

    institucion_asignada = forms.ModelChoiceField(
        queryset=Institucion.objects.all(),
        required=True, # Es requerido porque todos son 'usuario'
        label="Institución de Afiliación",
    )

    class Meta:
        model = Usuario
        # El formulario manejará estos campos del modelo
        fields = ('email', 'nombre', 'apellido', 'institucion_asignada')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # --- ESTA ES LA SOLUCIÓN AL DISEÑO ---
        # Definimos la clase de Tailwind que queremos aplicar
        tailwind_class = 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 mt-1'

        # Iteramos sobre todos los campos y aplicamos la clase
        # Esto funciona para <input> y <select>
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': tailwind_class})
        
        # --- SOLUCIÓN AL ORDEN ---
        # Forzamos el orden correcto de los campos
        self.field_order = ['email', 'nombre', 'apellido', 'rol', 'institucion_asignada']

    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Asignamos los campos personalizados
        user.rol = 'usuario'
        institucion = self.cleaned_data.get('institucion_asignada')
        
        if user.rol == 'usuario' and institucion:
            user.institucion_asignada = institucion
        else:
            user.institucion_asignada = None 

        if commit:
            user.save()
        return user