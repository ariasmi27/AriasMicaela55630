from django.shortcuts import render

from .models import vinos_tintos

# Create your views here.
def home(request):
    return render(request, "winesapp/home.html")

def vinos_tintos(request):
    #contexto = { 'vinos_tintos': vinos_tintos.objects.all() }
    return render(request, "winesapp/vinos_tintos.html")   

def vinos_blancos(request):
    return render(request, "winesapp/vinos_blancos.html")   

def vinos_espumantes(request):
    return render(request, "winesapp/vinos_espumantes.html")  

def vinos_rosados(request):
    return render(request, "winesapp/vinos_rosados.html")    