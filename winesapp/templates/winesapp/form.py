from django import forms

class vinosForm(forms.form):
   varietal = forms.CharField(max_length=50, required=True)
   cosecha = form.IntegerField(required=True)
   