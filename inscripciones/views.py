from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InscripcionForm
from .models import Inscripcion

@login_required
def inscribirse_materia(request):
    if request.user.rol != 'student':
        return redirect('home')  # o mostrar mensaje de error

    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.estudiante = request.user
            inscripcion.save()
            return redirect('lista_inscripciones')  # o cualquier vista que desees
    else:
        form = InscripcionForm()

    return render(request, 'inscripciones/inscribirse.html', {'form': form})