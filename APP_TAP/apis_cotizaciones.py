import requests
from datetime import timedelta
from django.utils import timezone
from .models import Cotizacion

def actualizacion_de_cotizaciones():
    ultima = Cotizacion.objects.order_by('-fecha_actualizacion').first()

    if ultima and timezone.now() - ultima.fecha_actualizacion < timedelta(minutes = 2):
        return

    respuesta = requests.get("https://dolarapi.com/v1/dolares")
    datos = respuesta.json()

    for item in datos:
        existente = Cotizacion.objects.filter(moneda = item["moneda"], casa = item["casa"]).first()

        compra_anterior = existente.compra if existente else None
        venta_anterior = existente.venta if existente else None

        Cotizacion.objects.update_or_create(
            moneda=item["nombre"],
            casa=item["casa"],
            defaults={
                "nombre": item["nombre"],
                "compra": item["compra"],
                "venta": item["venta"],
                "compra_anterior": compra_anterior,
                "venta_anterior": venta_anterior,
                "fecha_actualizacion": item["fechaActualizacion"],
            }
        )