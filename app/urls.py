from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
     path('inicio/', views.inicio, name="inicio")
]