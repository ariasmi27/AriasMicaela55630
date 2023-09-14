from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from django.template import loader
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView




# Create your views here.
def home(request):
    return render(request, "winesapp/home.html")

def vinos_tintos2(request):
    contexto = { 'vinos_tintos': vinos_tintos.objects.all() }
    return render(request, "winesapp/vinos_tintos.html", { 'vinos_tintos': vinos_tintos.objects.all() })   

def vinos_blancos2(request):
    contexto = { 'vinos_blancos': vino_blanco.objects.all() }
    return render(request, "winesapp/vinos_blancos.html", { 'vinos_blancos' : Vino_blanco.objects.all()})   

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
        vinos = vinos_blancos.objects.filter(varietal__icontains=patron)  
        contexto = { 'vinos_tintos': vinos_tintos }    
        return render(request,"winesapp/vinos_tintos.html", contexto)   
    return HttpResponse ("No se ingreso nada a buscar")          

def vinos_blancos2(request):
    contexto = { 'vinos_blancos': vinos_blancos.objects.all() }
    return render(request, "winesapp/vinos_blancos.html", { 'vinos_blancos': vinos_blancos.objects.all() }) 

def updateVino_blanco(request, id_vino_blanco):
    vino_blanco = Vino_blanco.objects.get(id=id_vino_blanco)
    if request.method == "POST":
        miForm = Vino_blancoForm(request.POST)
        if miForm.is_valid():
            vino_blanco.varietal = miForm.cleaned_data.get('varietal')
            vino_blanco.cosecha = miForm.cleaned_data.get('cosecha')
            vino_blanco.save()
            return redirect(reverse_lazy('vinos_blancos'))   
    else:
        miForm = Vino_blancoForm(initial={
            'varietal': vino_blanco.varietal,
            'cosecha': vino_blanco.cosecha,
            })
    return render(request, "winesapp/vino_blancoForm.html", {'form': miForm})   

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                return render(request, "winesapp/index.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "winesapp/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "winesapp/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "winesapp/login.html", {"form":miForm})    

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "winesapp/index.html")
    else:
        miForm = RegistroUsuariosForm()      
    return render(request, "winesapp/registro.html", {"form":miForm}) 


class Vino_espumanteList(ListView):
    model = vinos_espumantes

class Vino_espumanteCreate(CreateView):
    model = vinos_espumantes
    fields = ['varietal', 'cosecha']
    success_url = reverse_lazy('vinos_espumantes2')

class Vino_espumanteUpdate(UpdateView):
    model = vinos_espumantes 
    fields = ['varietal', 'cosecha']
    success_url = reverse_lazy('vinos_espumantes2')

class Vino_espumanteDelete(DeleteView):
    model = vinos_espumantes
    success_url = reverse_lazy('vinos_espumantes2')    