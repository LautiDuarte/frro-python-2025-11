from django.db import models

class TipoRecurso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    ubicacion = models.CharField(max_length=200)
    estado = models.CharField(max_length=20)

    tipo = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE, related_name="recursos")

    def __str__(self):
        return f"Recurso {self.id} - {self.tipo.nombre}"