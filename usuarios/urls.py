from django.urls import path
from . import views

app_name='usuarios'
urlpatterns = [
    path('', views.default, name='default'),
    path('login/', views.login_view, name='login'),
    path('user/home/', views.user_home, name='user_home'),
    path('administration/home/', views.admin_home, name='admin_home'),
]

