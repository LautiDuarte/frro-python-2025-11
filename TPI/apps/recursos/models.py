from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField(default=None)
    longitud = models.FloatField(default=None)
    tipo = models.CharField(max_length=50, default=None) 

    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    id = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=20)
    institucion_base = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name="recursos")
    def __str__(self):
        return f"Recurso {self.id} - {self.institucion_base.nombre}"