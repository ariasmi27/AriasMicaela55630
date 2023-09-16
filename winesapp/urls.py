from django.urls import path
from .views import *
from django.urls import include

urlpatterns = [
   path('', home, name="home"),
   path('vinos_tintos/', vinos_tintos2, name= "vinos_tintos"),
   
   path('vinos_rosados/', vinos_rosados2, name= "vinos_rosados"),
   path('vinos_espumantes/', vinos_espumantes2, name= "vinos_espumantes"),
   
   path('vinosForm/', vinos_abm, name= "vinosForm"),
   path('buscar_varietal/', buscar_varietal, name= "buscar_varietal"),
   path('buscar2/', buscar2, name= "buscar2"),

   path('vinos_blancos/', vinos_blancos2, name= "vinos_blancos"),
   path('update_vino_blanco/<id_vino_blanco>/', updateVino_blanco, name="update_vino_blanco" ),
   path('login/', login_request, name="login" ),

   path('vinos_espumantes/', Vino_espumanteList.as_view(), name="vinos_espumantes" ),

    path('create_vino_espumante/', Vino_espumanteCreate.as_view(), name="create_vino_espumante" ),    
    path('update_vino_espumante/<int:pk>/', Vino_espumanteUpdate.as_view(), name="update_vino_espumante" ),
    path('delete_vino_espumante/<int:pk>/', Vino_espumanteDelete.as_view(), name="delete_vino_espumante" ),

 
   ]