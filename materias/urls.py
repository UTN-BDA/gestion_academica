from django.urls import path
from . import views

app_name = 'materias' 

urlpatterns = [
    path('administration/carreras/', views.lista_carreras, name='carrera'),
    path('administration/materias/', views.lista_materias, name='materia'),
    path('administration/usuarios/', views.lista_usuarios, name='usuario')
]

     
