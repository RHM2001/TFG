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
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class EntidadMusicalViewSet(viewsets.ModelViewSet):
    queryset = EntidadMusical.objects.all()
    serializer_class = EntidadMusicalSerializer