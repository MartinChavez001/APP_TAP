import requests
from datetime import timedelta
from django.utils import timezone
from .models import Cotizacion
from django.utils.dateparse import parse_datetime
from decimal import Decimal

def actualizacion_de_cotizaciones():
    ultima = Cotizacion.objects.order_by('-fecha_actualizacion').first()

    if ultima and timezone.now() - ultima.fecha_actualizacion < timedelta(minutes = 2):
        return

    respuesta = requests.get("https://dolarapi.com/v1/dolares")
    datos = respuesta.json()

    for item in datos:
        criterios = {"moneda": "USD", "casa": item["casa"]}
        existente = Cotizacion.objects.filter(**criterios).first()
        nueva_fecha = parse_datetime(item["fechaActualizacion"])
        compra_anterior = None
        venta_anterior = None

        if existente:   
            if nueva_fecha < existente.fecha_actualizacion:
                continue

            if existente.compra != Decimal(str(item["compra"])):
                compra_anterior = existente.compra
                venta_anterior = existente.venta
            else:
                compra_anterior = existente.compra_anterior
                venta_anterior = existente.venta_anterior

        Cotizacion.objects.update_or_create(
            **criterios,
            defaults={
                "nombre": item["nombre"],
                "compra": item["compra"],
                "venta": item["venta"],
                "compra_anterior": compra_anterior,
                "venta_anterior": venta_anterior,
                "fecha_actualizacion": nueva_fecha,
            }
        )
