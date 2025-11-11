from django.contrib import admin
from .models import Incidente, Asignacion, TipoIncidente

class AsignacionInline(admin.TabularInline):
    """
    Permite ver y editar Asignaciones DIRECTAMENTE
    dentro de la página de un Incidente.
    """
    model = Asignacion
    extra = 1 # Muestra 1 slot vacío para añadir una nueva asignación
    autocomplete_fields = ['recurso'] # Facilita buscar recursos

@admin.register(Incidente)
class IncidenteAdmin(admin.ModelAdmin):
    """
    Configuración para Incidentes.
    """
    list_display = ('id', 'titulo', 'estado', 'gravedad', 'tipo', 'usuario', 'fecha_hora')
    search_fields = ('titulo', 'detalle')
    list_filter = ('estado', 'gravedad', 'tipo')
    
    # Añade el inline de Asignacion
    inlines = [AsignacionInline]

@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    """
    Configuración para Asignaciones (opcional, ya que está en Incidente).
    """
    list_display = ('id', 'incidente', 'recurso', 'fecha_hora_inicio', 'tiempo_estimado_llegada')
    list_filter = ('recurso',)
    autocomplete_fields = ['incidente', 'recurso']

# Registra el modelo simple
admin.site.register(TipoIncidente)