from django.shortcuts import render
from .models import Career
from django.contrib.auth import authenticate
# Create your views here.



# VISTA DE SITIO WEB

def home(request):
    return render(request, 'home.html')

# VISTAS PARA Usuarios

# VISTAS para Carreras

def lista_carreras(request):
    carreras = Career.objects.all()
    return render(request, 'carreras.html', {'carreras': carreras})

# VISTAS  de Usuario
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, 'login.html', {'success': 'Inicio de sesión exitoso.'})
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas.'})
    return render(request, 'login.html')