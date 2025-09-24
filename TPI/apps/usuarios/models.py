from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission

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

    # Redefinimos groups y user_permissions para evitar conflictos
    groups = models.ManyToManyField(
        Group,
        related_name="usuarios_usuario_groups",  # nombre único
        blank=True,
        help_text="Grupos a los que pertenece el usuario",
        verbose_name="grupos"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuarios_usuario_permissions",  # nombre único
        blank=True,
        help_text="Permisos específicos del usuario",
        verbose_name="permisos de usuario"
    )

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre", "apellido"]
    EMAIL_FIELD = "email"

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"
