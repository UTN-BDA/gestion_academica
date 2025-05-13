from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Inscripcion
from .models import Nota

class NotaInline(admin.TabularInline):
    model = Nota
    extra = 1

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'materia', 'fecha_inscripcion')
    search_fields = ('estudiante__first_name', 'materia__nombre')
    list_filter = ('fecha_inscripcion',)
    inlines = [NotaInline]

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('inscripcion', 'nota', 'fecha_carga')