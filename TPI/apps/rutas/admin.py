from django.contrib import admin
from .models import Ruta # Asumiendo que el modelo se llama Ruta

@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('id', 'origen', 'destino', 'tiempo_transito', 'estado')
    list_filter = ('estado',)
    search_fields = ('origen', 'destino')