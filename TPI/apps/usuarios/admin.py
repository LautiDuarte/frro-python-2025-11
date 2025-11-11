from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    """
    Configuración para mostrar el modelo Usuario en el panel de admin.
    """
    list_display = ('email', 'nombre', 'apellido', 'rol', 'institucion_asignada', 'is_staff')
    search_fields = ('email', 'nombre', 'apellido')
    list_filter = ('rol', 'institucion_asignada', 'is_staff', 'is_active')
    
    # Define los campos que se pueden editar
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'apellido', 'rol', 'institucion_asignada')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    # Define los campos al crear un nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'nombre', 'apellido', 'rol', 'institucion_asignada', 'is_staff', 'is_superuser'),
        }),
    )
    
    ordering = ('email',)