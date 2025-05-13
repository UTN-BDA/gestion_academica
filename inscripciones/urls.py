from django.urls import path
from . import views

urlpatterns = [
    path('inscribirse/', views.inscribirse_materia, name='inscribirse_materia'),
]