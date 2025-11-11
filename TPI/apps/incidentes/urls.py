from rest_framework.routers import DefaultRouter
from .views import IncidenteViewSet, AsignacionViewSet

router = DefaultRouter()
router.register(r'incidentes', IncidenteViewSet)
router.register(r'asignaciones', AsignacionViewSet)

urlpatterns = router.urls
