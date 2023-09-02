from django.urls import path
from .views import *
from django.urls import include

urlpatterns = [
   path('', home, name="home"),
   path('vinos_tintos/', vinos_tintos, name= "vinos_tintos"),
   path('vinos_blancos/', vinos_blancos, name= "vinos_blancos"),
   path('vinos_espumantes/', vinos_espumantes, name= "vinos_espumantes"),
   path('vinos_rosados/', vinos_rosados, name= "vinos_rosados"),
   ]