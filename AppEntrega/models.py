from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Auto(models.Model):
    Marca: models.CharField(max_length=20)
    Modelo: models.CharField(max_length=20)  # Desconozco Field para letras y números
    Patente: models.IntegerField()


class Propietario(models.Model):
    Nombre: models.CharField(max_length=20)
    Apellido: models.CharField(max_length=20)
    DNI: models.IntegerField()


class Ciudad(models.Model):
    Origen: models.CharField(max_length=20)
    Destino: models.CharField(max_length=20)
