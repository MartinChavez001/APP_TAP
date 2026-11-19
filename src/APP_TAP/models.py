from django.db import models
from django.conf import settings


class Cotizacion(models.Model):
    @property
    def variacion(self):
        if self.compra_anterior:
            return (self.compra - self.compra_anterior) / self.compra_anterior * 100
        return None

    moneda = models.CharField(max_length=10)
    casa = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50)
    compra = models.DecimalField(max_digits=10, decimal_places=2)
    venta = models.DecimalField(max_digits=10, decimal_places=2)
    compra_anterior = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank= True)
    venta_anterior = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank= True)
    fecha_actualizacion = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["moneda", "casa"], name="cotizacion_moneda_casa_unica"),
        ]

class Favorito(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    alias = models.CharField(max_length=50, blank=True, default="")
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cotizacion"], name="favorito_cotizacion_unica"),
        ]
