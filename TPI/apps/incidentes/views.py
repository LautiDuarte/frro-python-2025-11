from rest_framework import viewsets
from .models import Incidente, Asignacion
from .serializers import IncidenteSerializer, AsignacionSerializer

class IncidenteViewSet(viewsets.ModelViewSet):
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user, estado="Activo")

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer