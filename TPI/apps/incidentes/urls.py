from rest_framework.routers import DefaultRouter
from .views import TipoIncidenteViewSet, IncidenteViewSet, AsignacionViewSet

router = DefaultRouter()
router.register(r'tipos-incidentes', TipoIncidenteViewSet)
router.register(r'incidentes', IncidenteViewSet)
router.register(r'asignaciones', AsignacionViewSet)

urlpatterns = router.urls
