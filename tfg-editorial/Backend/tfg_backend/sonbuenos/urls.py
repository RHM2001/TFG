from django.urls import path, include
from rest_framework import routers
from .viewsets import SonBuenosViewSet, GeneroViewSet, EntidadMusicalViewSet, CancionViewSet, ArtistaViewSet, SolicitudViewSet
from .views import login_view
from .views import marcar_solicitud_como_tratada
from .views import eliminar_solicitud

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
    path('solicitudes/<int:solicitud_id>/marcar-tratada/', marcar_solicitud_como_tratada, name='marcar_tratada'),
    path('solicitudes/<int:solicitud_id>/eliminar_solicitud/', eliminar_solicitud, name='eliminar_solicitud'),
] + router.urls

