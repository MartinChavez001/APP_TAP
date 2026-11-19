from django.db import models
from django.conf import settings
from decimal import Decimal

@property
def variacion_porcentaje(self):
    if self.compra_anterior is None or self.compra_anterior == 0:
        return None

    variacion = (
        (self.compra - self.compra_anterior)
        / self.compra_anterior
    ) * Decimal("100")

    return abs(variacion)

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
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
