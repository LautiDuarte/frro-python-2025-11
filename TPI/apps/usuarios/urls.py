from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = router.urls