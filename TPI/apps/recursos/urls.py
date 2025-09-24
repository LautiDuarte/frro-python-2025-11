from rest_framework.routers import DefaultRouter
from .views import RecursoViewSet, TipoRecursoViewSet

router = DefaultRouter()
router.register(r'recursos', RecursoViewSet)
router.register(r'tipos-recursos', TipoRecursoViewSet)

urlpatterns = router.urls
