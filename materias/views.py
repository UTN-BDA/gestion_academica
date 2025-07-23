from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count  # 👈 AÑADIDO Count
from django.core.paginator import Paginator

from .forms import UsuarioForm, UsuarioCrearForm, CareerForm, MateriaForm
from usuarios.models import User
from .models import Career, Materia
from inscripciones.models import Inscripcion, InscripcionCarrera


@login_required
def lista_carreras(request):
    query = request.GET.get('buscar')
    if query:
        carreras_queryset = Career.objects.filter(Q(name__icontains=query))
    else:
        carreras_queryset = Career.objects.all()

    # ✅ Anotación para contar inscriptos
    carreras_queryset = carreras_queryset.annotate(num_inscriptos=Count('inscripcioncarrera'))

    paginator = Paginator(carreras_queryset, 10)
    page_number = request.GET.get('page')
    carreras = paginator.get_page(page_number)

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

    # ✅ Anotación para contar inscriptos
    materias = materias.annotate(num_inscriptos=Count('inscripcion'))

    paginator = Paginator(materias, 10)
    page_number = request.GET.get('page')
    materias_paginadas = paginator.get_page(page_number)

    return render(request, 'materias_admin.html', {'materias': materias_paginadas})


@login_required
def editar_materia(request, materia_id):
    materia = get_object_or_404(Materia, id=materia_id)

    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('materias:materia')
    else:
        form = MateriaForm(instance=materia)

    return render(request, 'editar_materia.html', {'form': form, 'materia': materia})


@login_required
def lista_usuarios(request):
    query = request.GET.get('buscar')
    if query:
        usuarios_queryset = User.objects.filter(
            Q(dni__icontains=query) |
            Q(email__icontains=query) |
            Q(last_name__icontains=query) |
            Q(first_name__icontains=query) |
            Q(career__name__icontains=query)
        )
    else:
        usuarios_queryset = User.objects.all()

    paginator = Paginator(usuarios_queryset, 10)
    page_number = request.GET.get('page')
    usuarios = paginator.get_page(page_number)

    return render(request, 'usuarios_admin.html', {'usuarios': usuarios})


@login_required
def materias_usuario(request):
    carrera_actual = request.user.career

    if carrera_actual:
        materias = Materia.objects.filter(carrera=carrera_actual)
    else:
        materias = Materia.objects.none()

    materias_inscriptas_ids = Inscripcion.objects.filter(estudiante=request.user).values_list('materia_id', flat=True)

    return render(request, 'materias_usuario.html', {
        'materias': materias,
        'materias_inscriptas_ids': materias_inscriptas_ids,
    })


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
        'carreras_inscriptas_ids': [i.carrera.id for i in inscripciones]
    })


@login_required
def inscribirse_carrera(request, carrera_id):
    carrera_nueva = get_object_or_404(Career, id=carrera_id)

    InscripcionCarrera.objects.filter(estudiante=request.user).delete()
    Inscripcion.objects.filter(estudiante=request.user).delete()

    InscripcionCarrera.objects.create(estudiante=request.user, carrera=carrera_nueva)
    request.user.career = carrera_nueva
    request.user.save()

    return redirect('materias:carreras_usuario')


@login_required
def inscribirse_materia(request, materia_id):
    materia = get_object_or_404(Materia, id=materia_id)

    if request.user.career != materia.carrera:
        return redirect('materias:materias_usuario')

    Inscripcion.objects.get_or_create(estudiante=request.user, materia=materia)
    return redirect('materias:materias_usuario')


@login_required
def ver_usuario(request, dni):
    usuario = get_object_or_404(User, dni=dni)
    materias_inscripto = Inscripcion.objects.filter(estudiante=usuario)

    if request.method == 'POST':
        if 'eliminar_usuario' in request.POST:
            usuario.delete()
            return redirect('materias:usuario')
        else:
            form = UsuarioForm(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                return redirect('materias:ver_usuario', dni=usuario.dni)
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'ver_usuario.html', {
        'usuario': usuario,
        'materias_inscripto': materias_inscripto,
        'form': form,
    })


@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioCrearForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(usuario.dni)
            usuario.save()
            return redirect('materias:usuario')
    else:
        form = UsuarioCrearForm()
    return render(request, 'crear_usuario.html', {'form': form})


@login_required
def crear_carrera(request):
    if request.method == 'POST':
        form = CareerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materias:carrera')
    else:
        form = CareerForm()
    return render(request, 'crear_carrera.html', {'form': form})


@login_required
def crear_materia(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materias:materia')
    else:
        form = MateriaForm()
    return render(request, 'crear_materia.html', {'form': form})


@login_required
def editar_carrera(request, carrera_id):
    carrera = get_object_or_404(Career, id=carrera_id)

    if request.method == 'POST':
        form = CareerForm(request.POST, instance=carrera)
        if form.is_valid():
            form.save()
            return redirect('materias:carrera')
    else:
        form = CareerForm(instance=carrera)

    return render(request, 'editar_carrera.html', {'form': form, 'carrera': carrera})