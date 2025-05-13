from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Asegurate de tener una vista llamada 'home'
        else:
            return render(request, 'usuarios/login.html', {'error': 'Credenciales inválidas.'})
    return render(request, 'usuarios/login.html')
