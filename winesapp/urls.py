from django.urls import path
from .views import *
from django.urls import include
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', home, name="home"),
   
   
   path('vinosForm/', vinos_abm, name= "vinosForm"),
   path('buscar_varietal/', buscar_varietal, name= "buscar_varietal"),
   path('buscar2/', buscar2, name= "buscar2"),

   path('vinos_blancos/', vinos_blancos2, name= "vinos_blancos"),
   path('update_vino_blanco/<id_vino_blanco>/', updateVino_blanco, name="update_vino_blanco" ),
   path('login/', login_request, name="login" ),
   path('logout/', LogoutView.as_view(template_name="winesapp/logout.html"), name="logout" ),
   path('registro/', register, name="registro" ),

   path('vinos_espumantes/', vinos_espumantesList.as_view(), name="vinos_espumantes" ),
   path('create_vino_espumante/', vinos_espumantesCreate.as_view(), name="create_vino_espumante" ),    
   path('update_vino_espumante/', vinos_espumantesUpdate.as_view(), name="update_vino_espumante" ),
   path('delete_vino_espumante/<int:pk>/', vinos_espumantesDelete.as_view(), name="delete_vino_espumante" ),
   path('editar_perfil/', editarPerfil, name="editar_perfil" ), 
   path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),

   path('vinos_rosados/', vinos_rosadosList.as_view(), name="vinos_rosados"),
   path('create_vino_rosado/', vinos_rosadosCreate.as_view(), name="create_vino_rosado" ), 

   path('vinos_tintos/', vinos_tintosList.as_view(), name="vinos_tintos"),
   path('create_vino_tinto/', vinos_tintosCreate.as_view(), name="create_vino_tinto" ),  

   ]