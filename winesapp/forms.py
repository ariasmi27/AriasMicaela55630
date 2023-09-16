from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class vinosForm(forms.Form):
   varietal = forms.CharField(max_length=50, required=True)
   cosecha = forms.IntegerField(required=True)
   
class vino_blancoForm(forms.Form):
   varietal = forms.CharField(label="Varietal", max_length=50, required=True)
   cosecha = forms.DateField(label="Cosecha", required=True)
   
class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
           