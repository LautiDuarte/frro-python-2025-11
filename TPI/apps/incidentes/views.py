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

        # Buscar recursos disponibles del tipo requerido
        recursos_disponibles = Recurso.objects.filter(
            estado="DISPONIBLE"
        )

        if not recursos_disponibles.exists():
            print("⚠️ No hay recursos disponibles para asignar al incidente.")
            return

        # Calcular la distancia de cada recurso al incidente
        recurso_mas_cercano = min(
            recursos_disponibles,
            key=lambda r: distancia_geografica(
                incidente.latitud, incidente.longitud, *r.get_posicion()
            )
        )

        # Asignar el recurso más cercano
        recurso_mas_cercano.estado = "OCUPADO"
        recurso_mas_cercano.save()

        Asignacion.objects.create(
            incidente=incidente,
            recurso=recurso_mas_cercano,
            tiempo_estimado_llegada=10,  # valor simbólico
        )

        incidente.estado = "ASIGNADO"
        incidente.save()

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer