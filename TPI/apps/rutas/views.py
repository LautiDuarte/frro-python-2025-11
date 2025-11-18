# tpi/apps/rutas/views.py
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Usamos OSRM public. Cambiá si tenés otro servidor.
OSRM_BASE = "https://router.project-osrm.org"  # usa https

@api_view(['GET'])
def ruta_mas_corta(request):
    """
    Query params:
      from_lat, from_lon, to_lat, to_lon
    Devuelve la geometría (GeoJSON LineString) y datos de tiempo/distancia.
    """
    try:
        from_lat = float(request.GET.get('from_lat'))
        from_lon = float(request.GET.get('from_lon'))
        to_lat = float(request.GET.get('to_lat'))
        to_lon = float(request.GET.get('to_lon'))
    except (TypeError, ValueError):
        return Response({"detail": "Parámetros inválidos. from_lat, from_lon, to_lat, to_lon requeridos."},
                        status=status.HTTP_400_BAD_REQUEST)

    # OSRM expects lon,lat pairs
    coords = f"{from_lon},{from_lat};{to_lon},{to_lat}"
    url = f"{OSRM_BASE}/route/v1/driving/{coords}?overview=full&geometries=geojson&steps=false"

    try:
        r = requests.get(url, timeout=8)
        r.raise_for_status()
        data = r.json()
        if 'routes' not in data or not data['routes']:
            return Response({"detail": "No se encontró ruta."}, status=status.HTTP_404_NOT_FOUND)

        route = data['routes'][0]
        return Response({
            "distance_m": route.get("distance"),
            "duration_s": route.get("duration"),
            "geometry": route.get("geometry")  # GeoJSON LineString
        })
    except requests.RequestException as e:
        return Response({"detail": f"Error al consultar el enrutador: {e}"},
                        status=status.HTTP_502_BAD_GATEWAY)
