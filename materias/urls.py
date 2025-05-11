from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
     path('home/', views.home, name="home"),
     path('carreras/', views.lista_carreras, name='carrera'),
     path('login/', views.login, name='login')
]