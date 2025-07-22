from django.urls import path
from . import views

app_name = 'materias'

urlpatterns = [
    path('administration/carreras/', views.lista_carreras, name='carrera'),
    path('administration/materias/', views.lista_materias, name='materia'),
    path('administration/usuarios/', views.lista_usuarios, name='usuario'),
    path('administration/usuario/<str:dni>/inscripciones/', views.ver_inscripciones, name='ver_inscripciones'),

    path('user/carreras/', views.carreras_usuario, name='carreras_usuario'),
    path('user/inscribirse_carrera/<int:carrera_id>/', views.inscribirse_carrera, name='inscribirse_carrera'),
    path('user/materias/', views.materias_usuario, name='materias_usuario'),
    path('user/inscribirse_materia/<int:materia_id>/', views.inscribirse_materia, name='inscribirse_materia'),
]
     
