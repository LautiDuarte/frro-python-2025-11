from rest_framework import viewsets
from .models import Recurso, Institucion, TipoRecurso
from .serializers import RecursoSerializer, InstitucionSerializer, TipoRecursoSerializer
from django.shortcuts import render

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class RecursoViewSet(viewsets.ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

class TipoRecursoViewSet(viewsets.ModelViewSet):
    queryset = TipoRecurso.objects.all()
    serializer_class = TipoRecursoSerializer
