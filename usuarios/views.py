from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from django.contrib import messages

def default(request):
    return redirect('usuarios:login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')
            if user.rol != 'admin':
                return redirect('usuarios:user_home')
            return redirect('usuarios:admin_home')
        else:
            messages.error(request, 'Credenciales invalidas')
            return render(request, 'login.html')
    return render(request, 'login.html')

def user_home(request):
    return render(request, 'user_home.html', {})

def admin_home(request):
    return render(request, 'admin_home.html', {})