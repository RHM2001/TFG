from django.db import models

# Create your models here.
class SonBuenos(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

class Artista (models.Model):
    nombre = models.CharField(max_length=50)

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
    idSpotify = models.CharField(max_length=50)
    entidad = models.ForeignKey(EntidadMusical, on_delete=models.CASCADE)

class Solicitud (models.Model):
    empresa = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    detalles = models.CharField(max_length=100)
    presupuesto = models.CharField(max_length=50)
    comentarios = models.CharField(max_length=50, null=True)
    tratado = models.BooleanField(default=False) 
    canciones = models.ManyToManyField(Cancion, null=True)
    
    
    
