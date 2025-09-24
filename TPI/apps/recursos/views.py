from rest_framework import viewsets
from .models import Recurso, TipoRecurso
from .serializers import RecursoSerializer, TipoRecursoSerializer

class TipoRecursoViewSet(viewsets.ModelViewSet):
    queryset = TipoRecurso.objects.all()
    serializer_class = TipoRecursoSerializer

class RecursoViewSet(viewsets.ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
