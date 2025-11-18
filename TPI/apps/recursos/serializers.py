from rest_framework import serializers
from .models import Recurso, Institucion

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = "__all__"

class RecursoSerializer(serializers.ModelSerializer):
    institucion_base = InstitucionSerializer()

    class Meta:
        model = Recurso
        fields = "__all__"

