from rest_framework import routers

from .viewsets import SonBuenosViewSet, GeneroViewSet, EntidadMusicalViewSet, CancionViewSet, ArtistaViewSet
router = routers.SimpleRouter()
router.register('sonbuenos', SonBuenosViewSet)
router.register('generos', GeneroViewSet)
router.register('canciones', CancionViewSet, basename='cancion')
router.register('entidades', EntidadMusicalViewSet)
router.register('artistas', ArtistaViewSet)


urlpatterns = router.urls