from django.contrib.auth.forms import UserCreationForm
from .models import Usuario 
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario 

class CustomUserCreationForm(UserCreationForm):
    class Meta: 
        model = Usuario
        fields = ('email', 'nombre', 'apellido', 'rol')