from django.shortcuts import render, redirect, get_object_or_404
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