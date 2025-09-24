from django.db import models
from apps.usuarios.models import Usuario

class TipoIncidente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Incidente(models.Model):
    titulo = models.CharField(max_length=100, default=None)
    detalle = models.TextField()
    gravedad = models.IntegerField()
    latitud = models.FloatField(default=None)
    longitud = models.FloatField(default=None)
    estado = models.CharField(max_length=20)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    tipo = models.ForeignKey(TipoIncidente, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="incidentes")

    def __str__(self):
        return f"Incidente {self.id} - {self.tipo.nombre}"

class Asignacion(models.Model):
    incidente = models.ForeignKey(Incidente, on_delete=models.CASCADE, related_name="asignaciones")
    recurso = models.ForeignKey("recursos.Recurso", on_delete=models.CASCADE, related_name="asignaciones")
    tiempo_estimado_llegada = models.IntegerField()
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Asignación {self.id} - Incidente {self.incidente.id}"
