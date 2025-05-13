from django.db import models

# Create your models here.

# inscripciones/models.py

from django.db import models
from usuarios.models import User
from materias.models import Materia

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
