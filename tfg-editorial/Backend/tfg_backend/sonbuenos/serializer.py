from .models import SonBuenos
from .models import Genero
from .models import Cancion
from .models import EntidadMusical
from .models import Artista
from .models import Solicitud
from rest_framework import serializers

class SonBuenosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SonBuenos
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Genero
        fields = '__all__'

class CancionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cancion
        fields = '__all__'

class EntidadMusicalSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EntidadMusical
        fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Artista
        fields = '__all__'

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Solicitud
        fields = '__all__'