from django.db import models

# Create your models here.

class Career(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
from django.db import models



class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    carrera = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return f"{self.nombre} ({self.carrera.name})"