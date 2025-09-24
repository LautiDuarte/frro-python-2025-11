from rest_framework.routers import DefaultRouter
from .views import RutaViewSet

router = DefaultRouter()
router.register(r'rutas', RutaViewSet)

urlpatterns = router.urls
