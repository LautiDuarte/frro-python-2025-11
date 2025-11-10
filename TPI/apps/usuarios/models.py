from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
# Importamos el modelo Recurso. Asegúrate de que esta ruta sea correcta para tu proyecto.
from apps.recursos.models import Institucion

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("rol", "admin") # Aseguramos que el superusuario sea admin
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=[
        ("admin", "Administrador"),
        ("operador", "Operador"),
        ("usuario", "Usuario"),
    ])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # ----------------------------------------------------
    # CAMBIO CLAVE: Relación 1 a 0/1 con INSTITUCION
    # ----------------------------------------------------
    institucion_asignada = models.ForeignKey(
        'recursos.Institucion', # <--- USA ESTA CADENA
        on_delete=models.SET_NULL, 
        related_name='usuarios_afiliados',
        null=True,                 
        blank=True                 
    )
    # ----------------------------------------------------

    # Redefinimos groups y user_permissions (mantenemos tu código)
    groups = models.ManyToManyField(
        Group,
        related_name="usuarios_usuario_groups",
        blank=True,
        help_text="Grupos a los que pertenece el usuario",
        verbose_name="grupos"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuarios_usuario_permissions",
        blank=True,
        help_text="Permisos específicos del usuario",
        verbose_name="permisos de usuario"
    )

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre", "apellido", "rol"] # Añadí 'rol' para asegurar que se pida al crear
    EMAIL_FIELD = "email"

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"