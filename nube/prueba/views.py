from django.shortcuts import render
from .models import carro
from .models import pastel
from .models import pizza
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms 
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
#Plantilla para listar carro
def base (request):
    template="base.html"
    return render (request, template)

def listar(request):
    carros= carro.objects.all()
    template="listar.html"
    context={
        'carros': carros,
    }
    return render (request,template,context)

#Plantilla para listar pizza
def listarpizza(request):
    pizzas= pizza.objects.all()
    template="pizza/listar.html"
    context={
        'pizza': pizzas,
    }
    return render (request, template, context)

#Plantilla para listar postre
def listarpostre(request):
    postre= pastel.objects.all()
    template="postre/listar.html"
    context={
        'postre': postre,
    }
    return render (request, template, context)

#Plantilla para crear carro
def carrocrear(request): 
    if request.method=='POST':
        form= agregar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    form = agregar 
    context={
        'form':form,
    }
    return render (request, "agregar.html", context)

#Plantilla para crear pizza
def crearpizza(request):
    if request.method=='POST':
        form= agregarpizza(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarpizza/')
    form = agregarpizza
    context={
        'form':form,
    }
    return render (request, "pizza/agregar.html", context) 

#Plantilla para crear postre
def crearpostre(request):
    if request.method=='POST':
        form= agregarpostre(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarpostre/')
    form = agregarpostre
    context={
        'form':form,
    }
    return render (request, "postre/agregar.html", context)

#Plantilla para eliminar carro por id
def eliminar(request, id):
    member = carro.objects.get(id=id)
    member.delete()
    return redirect(reverse('listar'))

#Plantilla para eliminar pizza por id
def eliminarpizza(request, id):
    edi = pizza.objects.get(id=id)
    edi.delete()
    return redirect('/listarpizza/')

#Plantilla para eliminar postre por id
def eliminarpostre(request, id):
    pos = pastel.objects.get(id=id)
    pos.delete()
    return redirect('/listarpostre/')

#Plantilla para actualizar coche
def actualizar(request, id):
    if request.method=='POST':
        instance=carro.objects.get(id=id)
        form=agregar(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('listar')
    dato = carro.objects.get(id=id)
    #form= agregar()
    #form=mymember
    template = 'actualizar.html'
    context = {
    'dato': dato,
    #'form':form,
    }
    return render(request, template, context)

#Plantilla para actualizar pizza
def actualizarpizza(request, id):
    if request.method=='POST':
        instance=pizza.objects.get(id=id)
        form=agregarpizza(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/listarpizza/')
    datos = pizza.objects.get(id=id)
    template = 'pizza/actualizar.html'
    context = {
        'datos':datos,
    }
    return render(request, template, context)

#Plantilla para actualizar postre
def actualizarpostre(request, id):
    if request.method=='POST':
        instancia=pastel.objects.get(id=id)
        form=agregarpostre(request.POST or None, instance= instancia)
        if form.is_valid():
            form.save()
            return redirect('/listarpostre/')
    datitos = pastel.objects.get(id=id)
    template = 'postre/actualizar.html'
    context = {
        'datitos': datitos,
    }
    return render(request, template, context)