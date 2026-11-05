from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('agregar-favoritos/', views.agregar_favoritos, name = 'agregar_favoritos'),
    path('elimar-favoritos/<int:favorito_id>', views.eliminar_favoritos, name = 'eliminar_favoritos'),
]
