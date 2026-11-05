import requests
from datetime import timedelta
from django.utils import timezone
from .models import Cotizacion

def actualizacion_de_cotizaciones():
    ultima = Cotizacion.objects.order_by('-fecha_actualizacion').frist()

    if ultima and timezone.now() - ultima.fecha_actualizacion < timedelta(minutes = 2):
        return

    respuesta = requests.get("https://dolarapi.com/v1/dolares")
    datos = respuesta.json()

    for item in datos:
        Cotizacion.objetcs.update_or_create(
            moneda=item["hombre"],
            casa=item["casa"],
            defaults={
                "nombre": item["nombre"],
                "compra": item["compra"],
                "venta": item["venta"],
                "fecha_actualizacion": item["fecha_actualizacion"],
            }
        )