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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




# Create your views here.
def home(request):
    return render(request, "winesapp/home.html")


@login_required
def vinos_tintos2(request):
    contexto = { 'vinos_tintos': vinos_tintos.objects.all() }
    return render(request, "winesapp/vinos_tintos.html", { 'vinos_tintos': vinos_tintos.objects.all() })   

@login_required
def vinos_blancos2(request):
    contexto = { 'vinos_blancos': vino_blanco.objects.all() }
    return render(request, "winesapp/vinos_blancos.html", { 'vinos_blancos' : vino_blanco.objects.all()})   

@login_required
def vinos_abm(request):
    if request.method == "POST":  
        vinos = vinos_tintos(varietal=request.POST['varietal'], 
                    cosecha=request.POST['cosecha'])  
        vinos.save()
        return HttpResponse("Se grabo con exito!")
    return render(request, "winesapp/vinosForm.html")    

@login_required
def buscar_varietal(request):
    return render(request, "winesapp/buscarVarietal.html")

@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET ['buscar']  
        vinos = vinos_blancos.objects.filter(varietal__icontains=patron)  
        contexto = { 'vinos_tintos': vinos_tintos }    
        return render(request,"winesapp/vinos_tintos.html", contexto)   
    return HttpResponse ("No se ingreso nada a buscar")          

@login_required
def vinos_blancos2(request):
    contexto = { 'vinos_blancos': vinos_blancos.objects.all() }
    return render(request, "winesapp/vinos_blancos.html", { 'vinos_blancos': vinos_blancos.objects.all() }) 


@login_required
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


#@login_required
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "winesapp/index.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "winesapp/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "winesapp/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "winesapp/login.html", {"form":miForm})    

#@login_required
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

class vinos_tintosList(ListView):
    model =vinos_tintos

class vinos_tintosCreate(CreateView):
    model = vinos_tintos
    fields = ['varietal', 'cosecha']
    success_url = reverse_lazy('vinos_tintos')


class vinos_rosadosList(ListView):
    model = vinos_rosados

class vinos_rosadosCreate(CreateView):
    model = vinos_rosados
    fields = ['varietal', 'cosecha']
    success_url = reverse_lazy('vinos_rosados')


class vinos_espumantesList(ListView):
    model = vinos_espumantes

class vinos_espumantesCreate(CreateView):
    model = vinos_espumantes
    fields = ['varietal', 'cosecha']
    success_url = reverse_lazy('vinos_espumantes')

class vinos_espumantesUpdate( UpdateView):
    model = vinos_espumantes 
    fields = ['varietal', 'cosecha']
    success_url = reverse_lazy('vinos_espumantes')

class vinos_espumantesDelete(LoginRequiredMixin, DeleteView):
    model = vinos_espumantes
    success_url = reverse_lazy('vinos_espumantes')    


#@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"winesapp/index.html")
        else:
            return render(request,"winesapp/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "winesapp/editarPerfil.html", {'form': form, 'usuario': usuario.username})

#@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

        
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

        
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"winesapp/index.html")
    else:
        form = AvatarFormulario()
    return render(request, "winesapp/agregarAvatar.html", {'form': form })


