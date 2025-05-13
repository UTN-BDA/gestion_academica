from django.shortcuts import render
from .models import Career
from django.contrib.auth import authenticate
# Create your views here.


# VISTAS para Carreras

def lista_carreras(request):
    carreras = Career.objects.all()
    return render(request, 'materias/carreras.html', {'carreras': carreras})

