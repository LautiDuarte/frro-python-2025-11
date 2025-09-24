from rest_framework import serializers
from .models import Incidente, TipoIncidente, Asignacion

class TipoIncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIncidente
        fields = "__all__"

class IncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidente
        fields = "__all__"

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = "__all__"
