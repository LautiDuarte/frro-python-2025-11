from django.utils import timezone
from apps.recursos.models import Recurso
from apps.incidentes.models import Incidente, Asignacion
from apps.incidentes.utils import distancia_geografica


def asignar_incidentes_pendientes():
    incidentes_pendientes = (
        Incidente.objects
        .filter(estado="PENDIENTE")
        .order_by('-gravedad', 'fecha_hora')
    )

    for incidente in incidentes_pendientes:
        recursos_disponibles = Recurso.objects.filter(
            estado="DISPONIBLE"
        )

        if not recursos_disponibles.exists():
            continue  # Ningún recurso disponible de ese tipo

        recurso_mas_cercano = min(
            recursos_disponibles,
            key=lambda r: distancia_geografica(
                incidente.latitud, incidente.longitud, *r.get_posicion()
            )
        )

        # Actualizar estados y registrar la asignación
        recurso_mas_cercano.estado = "OCUPADO"
        recurso_mas_cercano.save()

        Asignacion.objects.create(
            incidente=incidente,
            recurso=recurso_mas_cercano,
            tiempo_estimado_llegada=10,
            fecha_hora_inicio=timezone.now()
        )

        incidente.estado = "ASIGNADO"
        incidente.save()

def finalizar_asignacion(incidente_id):
    """
    Marca un incidente como FINALIZADO, libera el recurso asociado
    y establece la fecha/hora de finalización en la asignación.
    """
    try:
        asignacion = Asignacion.objects.filter(incidente_id=incidente_id).last()
        if not asignacion:
            return False, "No se encontró una asignación para este incidente."

        recurso = asignacion.recurso
        recurso.estado = "DISPONIBLE"
        recurso.save()

        asignacion.fecha_hora_fin = timezone.now()
        asignacion.save()

        incidente = asignacion.incidente
        incidente.estado = "FINALIZADO"
        incidente.save()

        return True, "Incidente finalizado correctamente."
    except Exception as e:
        return False, f"Error al finalizar la asignación: {e}"