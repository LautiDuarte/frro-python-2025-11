from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField(default=None)
    longitud = models.FloatField(default=None)

    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    # Explicit primary key so static analyzers (Pylance) know the `id` attribute exists.
    # The project sets DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' in settings,
    # so use BigAutoField here to match that default and avoid mismatches.
    id = models.BigAutoField(primary_key=True)
    
    estado = models.CharField(max_length=20)

    institucion_base = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name="recursos")

    def __str__(self):
        return f"Recurso {self.id} - {self.institucion_base.nombre}"