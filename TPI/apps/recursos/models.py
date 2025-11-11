from django.db import models
from django.conf import settings # Usar settings.AUTH_USER_MODEL es la mejor práctica si el modelo Usuario es el AUTH_USER_MODEL

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField(default=None, null=True, blank=True)
    longitud = models.FloatField(default=None, null=True, blank=True)

    def __str__(self):
        return self.nombre

# apps/recursos/models.py
class Recurso(models.Model):
    id = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=20, default='DISPONIBLE')
    institucion_base = models.ForeignKey(
        Institucion, on_delete=models.CASCADE, related_name="recursos"
    )
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)

    def get_posicion(self):
        return (self.latitud or self.institucion_base.latitud, 
                self.longitud or self.institucion_base.longitud)

    def __str__(self):
        return f"Recurso {self.id} | Base: {self.institucion_base.nombre}"
    
    