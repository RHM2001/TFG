from django.db import models

# Create your models here.
class SonBuenos(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

class Artista (models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50, null=True)

class Genero (models.Model):
    nombre = models.CharField(max_length=50)

class EntidadMusical (models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.ManyToManyField(Genero)
    artistas = models.ManyToManyField(Artista)

class Cancion (models.Model):
    nombre = models.CharField(max_length=50)
    url = models.URLField(null=True)
    genero = models.ManyToManyField(Genero)
    duracion = models.DurationField(null=True)
    fecha = models.DateField(null=True)
    entidad = models.OneToOneField(EntidadMusical, on_delete=models.CASCADE)
