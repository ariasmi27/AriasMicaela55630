from django import forms

class vinosForm(forms.Form):
   varietal = forms.CharField(max_length=50, required=True)
   cosecha = forms.IntegerField(required=True)
   
class vinos_blancosForm(forms.Form):
   varietal = forms.CharField(label="Nombre", max_length=50, required=True)
   cosecha = forms.DateField(label="Cosecha", required=True)
   