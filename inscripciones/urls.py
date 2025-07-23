from django.urls import path
from . import views

app_name = 'inscripciones'

urlpatterns = [
    path('inscribirse/', views.inscribirse_materia, name='inscribirse_materia'),
    path('notas/', views.lista_notas, name='lista_notas'),
]