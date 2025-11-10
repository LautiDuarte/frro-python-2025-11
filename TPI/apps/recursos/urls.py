from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecursoViewSet, InstitucionViewSet # Asegúrate de importar la función

# 1. Definir el Router de DRF
router = DefaultRouter()
router.register(r'recursos', RecursoViewSet)
router.register(r'instituciones', InstitucionViewSet) # Asumiré que quieres InstitucionViewSet en el path 'instituciones'

# 2. Obtener las URLs generadas por el Router
urlpatterns = router.urls

