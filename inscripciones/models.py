from django.db import models
from usuarios.models import User
from materias.models import Materia, Career


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'rol': 'student'})
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'materia')
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'

    def __str__(self):
        return f"{self.estudiante} inscrito en {self.materia}"


class InscripcionCarrera(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'rol': 'student'})
    carrera = models.ForeignKey(Career, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'carrera')
        verbose_name = 'Inscripción a Carrera'
        verbose_name_plural = 'Inscripciones a Carreras'

    def __str__(self):
        return f"{self.estudiante} inscrito en {self.carrera}"


class Nota(models.Model):
    inscripcion = models.ForeignKey('Inscripcion', on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    fecha_carga = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

    def __str__(self):
        return f"Nota {self.nota} - {self.inscripcion}"
