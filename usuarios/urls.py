from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='usuarios'
urlpatterns = [
    path('', views.default, name='default'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/home/', views.user_home, name='user_home'),
    path('administration/home/', views.admin_home, name='admin_home'),
    path('inicio/', views.user_home, name='user_home'),
]

