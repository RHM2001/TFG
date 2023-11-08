from rest_framework import viewsets

from .models import SonBuenos
from .serializer import SonBuenosSerializer

from .models import Genero
from .serializer import GeneroSerializer

from .models import Cancion
from .serializer import CancionSerializer

from .models import Artista
from .serializer import ArtistaSerializer

from .models import EntidadMusical
from .serializer import EntidadMusicalSerializer

class SonBuenosViewSet(viewsets.ModelViewSet):
    queryset = SonBuenos.objects.all()
    serializer_class = SonBuenosSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class CancionViewSet(viewsets.ModelViewSet):
    serializer_class = CancionSerializer

    def get_queryset(self):
        entidades_ids = self.request.query_params.getlist('entidades[]', [])
        generos_ids = self.request.query_params.getlist('generos[]', [])

        # Filtrar canciones por entidades y géneros seleccionados
        queryset = Cancion.objects.all()

        if entidades_ids:
            queryset = queryset.filter(entidad__id__in=entidades_ids)
        if generos_ids:
            queryset = queryset.filter(genero__id__in=generos_ids)

        return queryset
  

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class EntidadMusicalViewSet(viewsets.ModelViewSet):
    queryset = EntidadMusical.objects.all()
    serializer_class = EntidadMusicalSerializer