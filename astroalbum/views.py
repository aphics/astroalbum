from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def landing(request):
    return render(request, 'landing.html')


def login_view(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'msg': 'Usuario y/o contraseña incorrectos'})
    return render(request, 'login.html')


def register(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = User.objects.filter(username=username).exists()
        if user is True:
            return render(request, 'register.html', {'msg': 'Usuario registrado'})
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('home')
    return render(request, 'register.html')
