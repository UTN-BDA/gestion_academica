from django.shortcuts import render

from usuarios.models import User
from .models import Career, Materia
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def lista_carreras(request):
    carreras = Career.objects.all()
    return render(request, 'carreras_admin.html', {'carreras': carreras})

@login_required
def lista_materias(request):
    materias = Materia.objects.all()
    return render(request, 'materias_admin.html', {'materias': materias})

@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios_admin.html', {'usuarios': usuarios})

