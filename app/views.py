from django.shortcuts import render
from .models import Career
# Create your views here.



# VISTA DE SITIO WEB

def home(request):
    return render(request, 'home.html')

# VISTAS PARA Usuarios

# VISTAS para Carreras



def lista_carreras(request):
    carreras = Career.objects.all()
    return render(request, 'carreras.html', {'carreras': carreras})
# VISTAS    