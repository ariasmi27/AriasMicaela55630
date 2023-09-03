from django.shortcuts import render
from django.http import HttpResponse
from .models import vinos_tintos
from django.template import loader



# Create your views here.
def home(request):
    return render(request, "winesapp/home.html")

def vinos_tintos(request):
    contexto = { 'vinos_tintos': vinos_tintos.objects.all() }
    return render(request, "winesapp/vinos_tintos.html", { 'vinos_tintos': vinos_tintos.objects.all() })   

def vinos_blancos(request):
    return render(request, "winesapp/vinos_blancos.html")   

def vinos_espumantes(request):
    return render(request, "winesapp/vinos_espumantes.html")  

def vinos_rosados(request):
    return render(request, "winesapp/vinos_rosados.html")    

def inicio(request):

    contexto = {'vinos_tintos': vinos_tintos.objects.all()}
    plantilla = loader.get_template("winesapp/vinos_tintos.html")
    documento = plantilla.render( contexto )
    
    return HttpResponse( documento )    
