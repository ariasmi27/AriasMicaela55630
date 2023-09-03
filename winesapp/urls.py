from django.urls import path
from .views import *
from django.urls import include

urlpatterns = [
   path('', home, name="home"),
   path('vinos_tintos/', vinos_tintos, name= "vinos_tintos"),
   path('vinos_blancos/', vinos_blancos, name= "vinos_blancos"),
   path('vinos_rosados/', vinos_rosados, name= "vinos_rosados"),
   path('vinos_espumantes/', vinos_rosados, name= "vinos_espumantes"),
    path('inicio/', inicio, name= "inicio"),
   ]