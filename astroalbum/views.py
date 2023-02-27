from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .register_validator import user_validator, password_validator

# Create your views here.

def landing(request):
    """     Vista que despliega la página de bienvenida 

        Si el usuario está autenticado lo redirige a su home page

    Args:
        request (metodo http): Solicitud al servidor    

    Returns:
        render: Renderea landing.html
    """
    if request.user.is_authenticated:
        return redirect('home')
    
    return render(request, 'landing.html')


def login_view(request):
    """     Vista que despliega la página de login

        Si la solicitud al servidor es por el método GET se visualiza login.html
        En caso de que la solicitud al servidor sea por el método POST, se 
        autentica el usuario y la contraseña, en caso de ser correcta se redirije 
        al usuario a su home.html. En caso de que no se pueda autenticar al usuario
        se renderea de nuevo login.html y se le indica al usuario que su usuario
        y/o contraseña son incorrectos.
        Si el usuario está autenticado lo redirije a su home page

    Args:
        request (metodo http): Solicitud al servidor 

    Returns:
        render: Renderea home.html en caso de validar al usuario o
                renderea de nuevo login.html si el usuario no se logró validar
    """

    if request.user.is_authenticated:
        return redirect('home')
    
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
    """     Vista que despliega la página de registro

        Si la solicitud al servidor es por el método GET, se visualiza register.html
        En caso de que la solicitud sea por el método POST, se verifica que el nombre 
        de usuario no se encuentra ya en uso, de ser así lanza un mensaje de advertencia
        al usuario. Si el nombre de usuario no está en uso se procede a validar 
        los requerimentos del nombre de usuario y contraseña mediante los módulos
        user_validator y password_validator, respectivamente. Sí el nombre de
        usuario y el password son validados, se procede a crear un registro en la
        DB User, en caso cotrario se lanza un mensaje de advertencia al usuario.

        Si el usuario está autenticado lo redirije a su home page

    Args:
        request (metodo http): Solicitud al servidor

    Returns:
        render: Renderea home.html en caso de que el registro del usuario sea correcto
                en caso contrario renderea de nuevo register.html
    """
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        exist_user = User.objects.filter(username=username).exists()
        if exist_user is True:
            return render(request, 'register.html', {'msg': 'Nombre de usuario ya registrado'})
        else:
            valid_username = user_validator(username)
            valid_password = password_validator(password)
            if valid_username and valid_password:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'register.html', {'msg': 'Nombre de usuario y/o contraseña no validos'})
    return render(request, 'register.html')
