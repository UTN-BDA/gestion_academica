import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.core.management.base import BaseCommand
from faker import Faker
import random
from usuarios.models import User
from materias.models import Career, Materia
from inscripciones.models import Inscripcion

fake = Faker('es_AR')

class Command(BaseCommand):
    help = 'Genera registros de prueba en la base de datos.'

    def add_arguments(self, parser):
        parser.add_argument('--carreras', type=int, default=10, help='Cantidad de carreras')
        parser.add_argument('--materias', type=int, default=10, help='Cantidad de materias por carrera')
        parser.add_argument('--usuarios', type=int, default=50, help='Cantidad de usuarios')
        parser.add_argument('--inscripciones', type=int, default=10, help='Cantidad de inscripciones por usuario')

    def handle(self, *args, **options):
        cant_carreras = options['carreras']
        cant_materias = options['materias']
        cant_usuarios = options['usuarios']
        cant_inscripciones = options['inscripciones']

        # Genero Carreras
        self.stdout.write('*- Generando Carreras -*')
        carreras = []
        for _ in range(cant_carreras):
            nombre = f"{fake.word().capitalize()} {fake.word().capitalize()}"
            carrera = Career.objects.create(name=nombre)
            carreras.append(carrera)

        # Genero Materias
        self.stdout.write('*- Generando Materias -*')
        materias = []
        for carrera in carreras:
            for _ in range(cant_materias):
                nombre = f"{fake.word().capitalize()} {fake.word().capitalize()}"
                materia = Materia.objects.create(nombre = nombre, carrera = carrera)
                materias.append(materia)
        
        # Genero Usuarios
        self.stdout.write('*- Generando Usuarios -*')
        usuarios = []
        for _ in range (cant_usuarios):
            dni = fake.unique.random_int(min = 10000000, max = 49000000)
            user = User.objects.create_user(
                dni = str(dni),
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                email = fake.unique.email(),
                rol = 'student',
                career = random.choice(carreras)
            )
            usuarios.append(user)
        
        # Genero Inscripciones
        self.stdout.write('*- Generando Inscripciones -*')
        for user in usuarios:
            for _ in range(cant_inscripciones):
                materia = random.choice(materias)
                if not Inscripcion.objects.filter(estudiante=user, materia=materia).exists():
                    Inscripcion.objects.create(estudiante=user, materia=materia)
        
        self.stdout.write(self.style.SUCCESS('Datos generados correctamente.'))