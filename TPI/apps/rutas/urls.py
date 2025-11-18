from django.urls import path
from .views import ruta_mas_corta

urlpatterns = [
    path('rutas/route/', ruta_mas_corta, name='ruta-mas-corta'),
]
