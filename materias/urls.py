from django.urls import path
from . import views

app_name = 'materias'

urlpatterns = [
    path('carreras/', views.lista_carreras, name='carrera'),
    path('crear_carrera/', views.crear_carrera, name='crear_carrera'),

    path('materias/', views.lista_materias, name='materia'),
    path('crear_materia/', views.crear_materia, name='crear_materia'),
    path('editar_materia/<int:materia_id>/', views.editar_materia, name='editar_materia'),

    path('usuarios/', views.lista_usuarios, name='usuario'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('ver_usuario/<int:dni>/', views.ver_usuario, name='ver_usuario'),

    path('carreras_usuario/', views.carreras_usuario, name='carreras_usuario'),
    path('materias_usuario/', views.materias_usuario, name='materias_usuario'),

    path('inscribirse_carrera/<int:carrera_id>/', views.inscribirse_carrera, name='inscribirse_carrera'),
    path('inscribirse_materia/<int:materia_id>/', views.inscribirse_materia, name='inscribirse_materia'),
]
