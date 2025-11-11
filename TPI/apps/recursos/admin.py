from django.contrib import admin
from .models import Institucion, Recurso

@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    """
    Configuración para Instituciones (Hospitales, Bomberos, etc.)
    """
    list_display = ('nombre',  'latitud', 'longitud')
    search_fields = ('nombre',)
    list_filter = ()

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    """
    Configuración para Recursos (Ambulancias, etc.)
    """
    list_display = ('id', 'estado', 'institucion_base')
    search_fields = ('id', 'institucion_base__nombre')
    list_filter = ('estado', 'institucion_base')