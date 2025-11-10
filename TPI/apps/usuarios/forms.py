from django.contrib.auth.forms import UserCreationForm
from .models import Usuario 
from apps.recursos.models import Institucion # Importa el modelo Institucion
from django import forms # Necesitas esto para ModelChoiceField

class CustomUserCreationForm(UserCreationForm):
    # 1. Creamos un campo para la institución usando ModelChoiceField
    institucion_asignada = forms.ModelChoiceField(
        queryset=Institucion.objects.all(),
        required=False, # No es requerido aquí, será condicionalmente requerido por JS
        label="Institución de Afiliación",
        # El widget se renderizará como un <select>
    )

    class Meta:
        model = Usuario
        # Incluimos el nuevo campo en la lista de campos.
        # Quitamos 'rol' del 'fields' de la clase Meta, ya que lo vamos a inyectar con JS
        fields = ('email', 'nombre', 'apellido') # Dejamos solo los campos base, rol y recurso van por JS/custom
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 2. Re-agregamos el campo 'rol' como ChoiceField para tener el desplegable.
        # Aunque el campo 'rol' está en el modelo, lo definimos aquí para tener control.
        self.fields['rol'] = forms.ChoiceField(
            choices=Usuario.rol.field.choices,
            label='Rol de Usuario',
            required=True
        )

    # 3. Guardamos el campo de institución en la instancia de Usuario si existe en los datos
    def save(self, commit=True):
        user = super().save(commit=False)
        
        # La Institución ya viene en cleaned_data, la asignamos
        institucion = self.cleaned_data.get('institucion_asignada')
        
        # Asignamos el rol, que viene de la data
        user.rol = self.cleaned_data.get('rol')
        
        if user.rol == 'usuario' and institucion:
            user.institucion_asignada = institucion
        elif user.rol != 'usuario':
            user.institucion_asignada = None # Aseguramos que no tenga institución si no es usuario

        if commit:
            user.save()
        return user