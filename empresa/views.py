from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    Navbars = Navbar.objects.all()
    context = {
        "Navbars": Navbars

    }
    return render (request, 'empresa/index.html', context)

def Servicios(request):
    Navbars = Navbar.objects.all() # SELECT * FROM empresa_navbar
    Empresas = Empresa.objects.all()
    Trabajadores = Trabajador.objects.all()  
    Servicios = Servicio.objects.all()
    context = {
        "Navbars": Navbars,
        "Empresas": Empresas,
        "Trabajadores" : Trabajadores,
        "Servicios" : Servicios
    }
    return render (request, 'empresa/servicios.html', context)

def QuienesSomos(request):
    Navbars = Navbar.objects.all() # SELECT * FROM empresa_navbar
    Empresas = Empresa.objects.all()
    Trabajadores = Trabajador.objects.all()  
    Servicios = Servicio.objects.all()
    context = {
        "Navbars": Navbars,
        "Empresas": Empresas,
        "Trabajadores" : Trabajadores,
        "Servicios" : Servicios
    }
    return render (request, 'empresa/quienesSomos.html', context)