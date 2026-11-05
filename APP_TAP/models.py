from django.db import models
from django.conf import settings

class Cotizacion(models.Model):
    moneda = models.CharField(max_length=10)
    casa = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50)
    compra = models.DecimalField(max_digits=10, decimal_places=2)
    venta = models.DecimalField(max_digits=10, decimal_places=2)
    compra_anterior = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank= True)
    venta_anterior = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank= True)
    fecha_actualizacion = models.DateTimeField()

class Favorito(models.Model):
    Cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
