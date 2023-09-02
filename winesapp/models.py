from django.db import models

# Create your models here.

class vinos_tintos(models.Model):
    varietal = models.CharField(max_length=50)
    cosecha = models.DateField()

class vinos_blancos(models.Model):
    varietal = models.CharField(max_length=50) 
    cosecha = models.DateField()

class vinos_rosados(models.Model):
    varietal = models.CharField(max_length=50)    
    cosecha = models.DateField()

class vinos_espumantes(models.Model):
    varietal = models.CharField(max_length=50) 
    cosecha = models.DateField() 

     
