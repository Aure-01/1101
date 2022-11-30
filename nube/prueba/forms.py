from multiprocessing.sharedctypes import Value
from urllib import request
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class agregar(forms.ModelForm):
	class Meta:
		model=carro
		fields= ['id','color','modelo','anio','marca']

class agregarpizza(forms.ModelForm):
	class Meta:
		model=pizza
		fields= ['id_pizza', 'ingredientes', 'especialidad', 'tamanio', 'precio']

class agregarpostre(forms.ModelForm):
	class Meta:
		model=pastel
		fields= ['id_pastel', 'sabor', 'disenio', 'tamanio', 'precio']