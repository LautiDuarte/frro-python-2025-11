# En usuarios/forms.py

from django.contrib.auth.forms import UserCreationForm
# Importamos tu modelo de usuario personalizado.
# Usamos el punto (.) porque el modelo está en el mismo directorio.
from .models import Usuario 

# En usuarios/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import Usuario 

class CustomUserCreationForm(UserCreationForm):
    class Meta: # NOTA: Quitamos la herencia de UserCreationForm.Meta
        model = Usuario
        
        # 1. Definimos explícitamente los campos que deben aparecer en el formulario.
        #    Usamos el 'email' en lugar del 'username'
        #    La contraseña y su confirmación se manejan automáticamente por UserCreationForm.
        fields = ('email', 'nombre', 'apellido', 'rol') # Agrega 'rol' si lo necesitas

    # OPCIONAL: Si no quieres que 'rol' aparezca en el registro, simplemente quítalo de 'fields'.