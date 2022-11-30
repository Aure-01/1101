from django.db import models
from  django.conf import settings


# Create your models here.
class carro(models.Model):
    color=models.CharField(max_length=20, blank=True, null=True)
    modelo= models.CharField(max_length=20, blank=True, null=True)
    anio= models.IntegerField()
    marca=models.CharField(max_length=20, blank=True, null=True)

class pastel(models.Model):
    id_pastel=models.IntegerField();
    sabor=models.CharField(max_length=20, blank=True, null=True)
    disenio=models.CharField(max_length=20, blank=True, null=True)
    tamanio=models.CharField(max_length=20, blank=True, null=True)
    precio=models.IntegerField()

class pizza(models.Model):
    id_pizza=models.IntegerField()
    ingredientes=models.CharField(max_length=50, blank=True, null=True)
    especialidad=models.CharField(max_length=20, blank=True, null=True)
    tamanio=models.CharField(max_length=20, blank=True, null=True)
    precio=models.IntegerField()