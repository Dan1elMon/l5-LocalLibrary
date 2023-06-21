from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # ...otras rutas de la aplicación catalog...
]