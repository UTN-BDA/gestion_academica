from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')  # Agregar mensaje de éxito
            return redirect('home')  # Redirigir a la página principal
        else:
            return render(request, 'usuarios/login.html', {'error': 'Credenciales inválidas.'})
    return render(request, 'usuarios/login.html')

