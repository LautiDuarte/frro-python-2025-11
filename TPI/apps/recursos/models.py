from django.db import models
from django.conf import settings # Usar settings.AUTH_USER_MODEL es la mejor práctica si el modelo Usuario es el AUTH_USER_MODEL

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField(default=None, null=True, blank=True)
    longitud = models.FloatField(default=None, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    estado = models.CharField(max_length=20)

    institucion_base = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name="recursos")
    
    # Se combina la salida y se maneja el caso NULL
    def __str__(self):
        # Muestra 'SIN ASIGNAR' si el campo es NULL
        return f"Recurso {self.id} | Base: {self.institucion_base.nombre}"