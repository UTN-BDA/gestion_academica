from django.urls import path
from . import views

app_name = 'materias'

urlpatterns = [
    path('administration/carreras/', views.lista_carreras, name='carrera'),
    path('administration/materias/', views.lista_materias, name='materia'),
    path('administration/usuarios/', views.lista_usuarios, name='usuario'),
    path('administration/usuario/crear/', views.crear_usuario, name='crear_usuario'),
    path('administration/usuario/<str:dni>/', views.ver_usuario, name='ver_usuario'),
    path('administration/carrera/crear/', views.crear_carrera, name='crear_carrera'),
    path('administration/materia/crear/', views.crear_materia, name='crear_materia'),

    path('user/carreras/', views.carreras_usuario, name='carreras_usuario'),
    path('user/inscribirse_carrera/<int:carrera_id>/', views.inscribirse_carrera, name='inscribirse_carrera'),
    path('user/materias/', views.materias_usuario, name='materias_usuario'),
    path('user/inscribirse_materia/<int:materia_id>/', views.inscribirse_materia, name='inscribirse_materia'),
]
     
