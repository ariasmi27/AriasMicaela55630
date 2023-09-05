from django.urls import path
from .views import *
from .views import vinos_blancos2
from django.urls import include

urlpatterns = [
   path('', home, name="home"),
   path('vinos_tintos/', vinos_tintos2, name= "vinos_tintos"),
   
   path('vinos_rosados/', vinos_rosados2, name= "vinos_rosados"),
   path('vinos_espumantes/', vinos_rosados2, name= "vinos_espumantes"),
   path('vinosForm/', vinos_abm, name= "vinosForm"),
   path('buscar_varietal/', buscar_varietal, name= "buscar_varietal"),
   path('buscar2/', buscar2, name= "buscar2"),

   path('vinos_blancos/', vinos_blancos2, name= "vinos_blancos"),
   ]