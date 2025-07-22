from django.shortcuts import render, redirect, get_object_or_404

from usuarios.models import User
from .models import Career, Materia
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from inscripciones.models import Inscripcion
from inscripciones.models import InscripcionCarrera
# Create your views here.

@login_required
def lista_carreras(request):
    query = request.GET.get('buscar')
    if query:
        carreras = Career.objects.filter(
            Q(name__icontains=query)
        )
    else:
        carreras = Career.objects.all()
    return render(request, 'carreras_admin.html', {'carreras': carreras})

@login_required
def lista_materias(request):
    query = request.GET.get('buscar')
    if query:
        materias = Materia.objects.filter(
            Q(nombre__icontains=query) |
            Q(carrera__name__icontains=query)
        )
    else:
        materias = Materia.objects.all()
    return render(request, 'materias_admin.html', {'materias': materias})

@login_required
def lista_usuarios(request):
    query = request.GET.get('buscar')
    if query:
        usuarios = User.objects.filter(
            Q(dni__icontains=query) |
            Q(email__icontains=query) |
            Q(last_name__icontains=query) |
            Q(first_name__icontains=query)
        )
    else:
        usuarios = User.objects.all()
    return render(request, 'usuarios_admin.html', {'usuarios': usuarios})

@login_required
def materias_usuario(request):
    carrera_actual = request.user.career  # o el campo que tengas para la carrera

    if carrera_actual:
        materias = Materia.objects.filter(carrera=carrera_actual)
    else:
        materias = Materia.objects.none()

    materias_inscriptas_ids = Inscripcion.objects.filter(estudiante=request.user).values_list('materia_id', flat=True)

    context = {
        'materias': materias,
        'materias_inscriptas_ids': materias_inscriptas_ids,
    }
    return render(request, 'materias_usuario.html', context)

@login_required
def carreras_usuario(request):
    carreras = Career.objects.all()
    inscripciones = InscripcionCarrera.objects.filter(estudiante=request.user).select_related('carrera')

    if request.method == "POST":
        carrera_id = request.POST.get("carrera_id")
        carrera = Career.objects.get(id=carrera_id)
        InscripcionCarrera.objects.get_or_create(estudiante=request.user, carrera=carrera)
        return redirect('materias:carreras_usuario')

    return render(request, 'carreras_usuario.html', {
        'carreras': carreras,
        'carreras_inscriptas_ids': [i.carrera.id for i in inscripciones]  # <-- Cambiado aquí
    })

@login_required
def inscribirse_carrera(request, carrera_id):
    carrera_nueva = get_object_or_404(Career, id=carrera_id)

    # Borrar inscripción anterior
    InscripcionCarrera.objects.filter(estudiante=request.user).delete()
    Inscripcion.objects.filter(estudiante=request.user).delete()  # borra materias inscritas

    # Crear nueva inscripción
    InscripcionCarrera.objects.create(estudiante=request.user, carrera=carrera_nueva)

    # Actualizar campo en User (usar el mismo nombre que en el modelo)
    request.user.career = carrera_nueva
    request.user.save()

    return redirect('materias:carreras_usuario')

@login_required
def inscribirse_materia(request, materia_id):
    materia = get_object_or_404(Materia, id=materia_id)

    # Verificar que la materia pertenezca a la carrera actual del usuario
    if request.user.career != materia.carrera:
        return redirect('materias:materias_usuario')

    Inscripcion.objects.get_or_create(estudiante=request.user, materia=materia)

    return redirect('materias:materias_usuario')

@login_required
def ver_inscripciones(request, dni):
    usuario = get_object_or_404(User, dni=dni)
    materias_inscripto = Inscripcion.objects.filter(estudiante=usuario)
    return render(request, 'ver_inscripciones.html', {
        'usuario': usuario,
        'materias_inscripto': materias_inscripto,
    })