from django.urls import path, include
from rest_framework import routers
from .viewsets import SonBuenosViewSet, GeneroViewSet, EntidadMusicalViewSet, CancionViewSet, ArtistaViewSet, SolicitudViewSet
from .views import login_view

from .viewsets import SonBuenosViewSet, GeneroViewSet, EntidadMusicalViewSet, CancionViewSet, ArtistaViewSet, SolicitudViewSet
router = routers.SimpleRouter()
router.register('sonbuenos', SonBuenosViewSet)
router.register('generos', GeneroViewSet)
router.register('canciones', CancionViewSet, basename='cancion')
router.register('entidades', EntidadMusicalViewSet)
router.register('artistas', ArtistaViewSet)
router.register('solicitudes', SolicitudViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
] + router.urls

