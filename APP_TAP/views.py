from django.shortcuts import render, redirect
from .apis_cotizaciones import actualizacion_de_cotizaciones
from .models import Cotizacion, Favorito

def index(request):
    return render(request, 'index.html')

def pagina_principal(request):
    actualizacion_de_cotizaciones()

    favorito = Favorito.objects.all()

    return render(request, 'index.html', {'favoritos': favoritos})
