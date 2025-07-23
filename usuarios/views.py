from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from usuarios.models import User  
from materias.models import Materia, Career  
from django.contrib import messages
from inscripciones.models import Inscripcion, Nota, InscripcionCarrera

def default(request):
    return redirect('usuarios:login')

def login_view(request):
    # Verifico si existe sesion iniciada
    if request.user.is_authenticated:
        if request.user.rol != 'admin':
            return redirect('usuarios:user_home')
        return redirect('usuarios:admin_home')
    
    # Compruebo credenciales
    if 'next' in request.GET:
        messages.warning(request, 'Sesion expirada. Iniciar sesion nuevamente.')
        return redirect('usuarios:login')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.rol != 'admin':
                return redirect('usuarios:user_home')
            return redirect('usuarios:admin_home')
        else:
            messages.error(request, 'Credenciales invalidas')
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required
def user_home(request):
    return render(request, 'user_home.html', {})

@login_required
def admin_home(request):
    if request.user.rol != 'admin':
        return redirect('usuarios:user_home')

    total_usuarios = User.objects.count()
    total_materias = Materia.objects.count()
    total_carreras = Career.objects.count()
    ultimos_usuarios = User.objects.order_by('-date_joined')[:5]  # o '-id' si no tenés date_joined

    context = {
        'total_usuarios': total_usuarios,
        'total_materias': total_materias,
        'total_carreras': total_carreras,
        'ultimos_usuarios': ultimos_usuarios,
    }

    return render(request, 'usuarios/admin_home.html', context)

@login_required
def user_home(request):
    estudiante = request.user

    # Obtener carrera del usuario (si está inscrito)
    ins_carrera = InscripcionCarrera.objects.filter(estudiante=estudiante).first()
    carrera = ins_carrera.carrera if ins_carrera else None

    # Obtener inscripciones a materias
    inscripciones = Inscripcion.objects.filter(estudiante=estudiante)

    # Obtener últimas notas
    notas = Nota.objects.filter(inscripcion__estudiante=estudiante).order_by('-fecha_carga')[:5]

    return render(request, 'usuarios/user_home.html', {
        'carrera': carrera,
        'inscripciones': inscripciones,
        'notas': notas,
    })