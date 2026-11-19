from django.db import migrations, models
from django.db.models import F, Q


def unificar_cotizaciones(apps, schema_editor):
    Cotizacion = apps.get_model("APP_TAP", "Cotizacion")
    Favorito = apps.get_model("APP_TAP", "Favorito")
    alias = schema_editor.connection.alias
    cotizaciones = Cotizacion.objects.using(alias)
    favoritos = Favorito.objects.using(alias)

    # La importación anterior guardaba el nombre del dólar en moneda.
    casas_dolar = ("oficial", "blue", "bolsa", "contadoconliqui", "mayorista", "cripto", "tarjeta")
    cotizaciones.filter(casa__in=casas_dolar).filter(
        Q(moneda=F("nombre")) | Q(moneda="")
    ).update(moneda="USD")

    duplicados = list(
        cotizaciones.values("moneda", "casa")
        .annotate(total=models.Count("pk"))
        .filter(total__gt=1)
    )
    for grupo in duplicados:
        filas = list(
            cotizaciones.filter(moneda=grupo["moneda"], casa=grupo["casa"])
            .order_by("-fecha_actualizacion", "-pk")
        )
        vigente, *anteriores = filas
        ids_anteriores = [fila.pk for fila in anteriores]
        favoritos_del_grupo = favoritos.filter(cotizacion_id__in=[vigente.pk, *ids_anteriores])
        favorito = favoritos_del_grupo.order_by("fecha_agregado", "pk").first()
        if favorito:
            favoritos_del_grupo.exclude(pk=favorito.pk).delete()
            favoritos.filter(pk=favorito.pk).update(cotizacion_id=vigente.pk)
        cotizaciones.filter(pk__in=ids_anteriores).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("APP_TAP", "0002_rename_cotizacion_favorito_cotizacion"),
    ]

    operations = [
        migrations.RunPython(unificar_cotizaciones),
        migrations.AddConstraint(
            model_name="cotizacion",
            constraint=models.UniqueConstraint(
                fields=["moneda", "casa"], name="cotizacion_moneda_casa_unica"
            ),
        ),
    ]
