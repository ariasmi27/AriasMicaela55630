from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader



# Create your views here.
def home(request):
    return render(request, "winesapp/home.html")

def vinos_tintos2(request):
    contexto = { 'vinos_tintos': vinos_tintos.objects.all() }
    return render(request, "winesapp/vinos_tintos.html", { 'vinos_tintos': vinos_tintos.objects.all() })   

def vinos_blancos2(request):
    contexto = { 'vinos_blancos': vinos_blancos.objects.all() }
    return render(request, "winesapp/vinos_blancos.html", { 'vinos_blancos' : vinos_blancos.objects.all()})   

def vinos_espumantes2(request):
    return render(request, "winesapp/vinos_espumantes.html")  

def vinos_rosados2(request):
    return render(request, "winesapp/vinos_rosados.html")    

def vinos_abm(request):
    if request.method == "POST":  
        vinos = vinos_tintos(varietal=request.POST['varietal'], 
                    cosecha=request.POST['cosecha'])  
        vinos.save()
        return HttpResponse("Se grabo con exito!")
    return render(request, "winesapp/vinosForm.html")    

def buscar_varietal(request):
    return render(request, "winesapp/buscarVarietal.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET ['buscar']  
        vinos = vinos_tintos.objects.filter(varietal__icontains=patron)  
        contexto = { 'vinos_tintos': vinos_tintos }    
        return render(request,"winesapp/vinos_tintos.html", contexto)   
    return HttpResponse ("No se ingreso nada a buscar")          

def vinos_blancos2(request):
    ctx = {'vinos_blancos': vinos_blancos.objects.all()}
    return render(request, "winesapp/vinos_blancos.html", ctx)
