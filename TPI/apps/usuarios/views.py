from rest_framework import viewsets, permissions
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        # 👇 Permitimos crear usuario sin estar autenticado
        if self.action == "create":
            return [permissions.AllowAny()]
        # 👇 El resto requiere estar autenticado
        return [permissions.IsAuthenticated()]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
