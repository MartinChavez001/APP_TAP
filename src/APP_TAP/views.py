from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .apis_cotizaciones import actualizacion_de_cotizaciones
from .models import Cotizacion, Favorito

def index(request):
    actualizacion_de_cotizaciones()

    favoritos = Favorito.objects.all()
    todas_las_cotizaciones = Cotizacion.objects.all()
    
    return render(request, 'index.html', {
        'favoritos': favoritos,
        'cotizaciones': todas_las_cotizaciones,
        })

@require_POST
def editar_favorito(request, favorito_id):
    favorito = get_object_or_404(Favorito, pk=favorito_id)
    alias = request.POST.get("alias", "").strip()

    if len(alias) <= 50:
        favorito.alias = alias
        favorito.save(update_fields=["alias"])

    return redirect("index")

def agregar_favoritos(request):
    if request.method == 'POST':
        cotizacion_id = request.POST.get('cotizacion_id')
        cotizacion = get_object_or_404(Cotizacion, id = cotizacion_id)

        Favorito.objects.get_or_create(cotizacion = cotizacion)

    return redirect('index')

def eliminar_favoritos(request, favorito_id):
    if request.method == 'POST':
        favorito = get_object_or_404(Favorito, id = favorito_id)
        favorito.delete()

    return redirect('index')