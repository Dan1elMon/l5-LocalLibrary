from django.urls import path
from . import views

urlpatterns = [
    # Patrón de URL corregido sin barra diagonal inicial
    path('', views.home, name='home'),  
    # Otros patrones de URL aquí...
]