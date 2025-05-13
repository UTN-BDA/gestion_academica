from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Inscripcion

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'materia', 'fecha_inscripcion')
    search_fields = ('estudiante__first_name', 'materia__nombre')
    list_filter = ('fecha_inscripcion',)