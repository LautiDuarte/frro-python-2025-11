from apps.incidentes.services import asignar_incidentes_pendientes
from apps.incidentes.utils import distancia_geografica
from apps.recursos.models import Recurso
from rest_framework import viewsets
from .models import Incidente, Asignacion
from .serializers import IncidenteSerializer, AsignacionSerializer

class IncidenteViewSet(viewsets.ModelViewSet):
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

    def perform_create(self, serializer):
        incidente = serializer.save(usuario=self.request.user, estado="PENDIENTE")

        asignar_incidentes_pendientes()

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.select_related('recurso__institucion_base','incidente').all()
    serializer_class = AsignacionSerializer