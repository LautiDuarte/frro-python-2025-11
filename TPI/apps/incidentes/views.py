from rest_framework import viewsets
from .models import Incidente, TipoIncidente, Asignacion
from .serializers import IncidenteSerializer, TipoIncidenteSerializer, AsignacionSerializer
from django.http import JsonResponse

class TipoIncidenteViewSet(viewsets.ModelViewSet):
    queryset = TipoIncidente.objects.all()
    serializer_class = TipoIncidenteSerializer

class IncidenteViewSet(viewsets.ModelViewSet):
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user, estado="Activo")

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer