from rest_framework.routers import DefaultRouter
from .views import RecursoViewSet, InstitucionViewSet

router = DefaultRouter()
router.register(r'recursos', RecursoViewSet)
router.register(r'tipos-recursos', InstitucionViewSet)

urlpatterns = router.urls
