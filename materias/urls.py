from django.urls import path
from . import views

app_name = 'materias' 

urlpatterns = [
    path('carreras/', views.lista_carreras, name='carrera'),  
]

     
