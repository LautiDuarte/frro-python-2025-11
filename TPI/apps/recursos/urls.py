from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecursoViewSet, InstitucionViewSet

# 1. Definir el Router de DRF
router = DefaultRouter()
router.register(r'recursos', RecursoViewSet)
router.register(r'instituciones', InstitucionViewSet)

# 2. Obtener las URLs generadas por el Router
urlpatterns = router.urls

