from rest_framework.routers import DefaultRouter
from .views import RecursoViewSet, InstitucionViewSet, TipoRecursoViewSet

router = DefaultRouter()
router.register(r'recursos', RecursoViewSet)
router.register(r'instituciones', InstitucionViewSet)
router.register(r'tipos-recursos', TipoRecursoViewSet)

urlpatterns = router.urls
