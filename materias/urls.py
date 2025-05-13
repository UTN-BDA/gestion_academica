from django.urls import path
from . import views

app_name = 'materias'  # Define el app_name aquí

urlpatterns = [
    path('carreras/', views.lista_carreras, name='carrera'),  # Asegúrate de que este 'name' esté correctamente definido
]

     
