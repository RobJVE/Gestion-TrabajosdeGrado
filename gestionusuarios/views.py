from django.shortcuts import render, redirect
from django.http import HttpResponse
from gestionusuarios.forms import UsuarioForm, PropuestaForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'gestionusuarios/home.html')
    return redirect('/login')


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "gestionusuarios/login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


def usuario_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = UsuarioForm()

        return render(request, 'gestionusuarios/nuevapersona.html', {'form':form})
    return redirect('/login')


def propuesta_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PropuestaForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = PropuestaForm()

        return render(request, 'gestionusuarios/nuevapropuesta.html', {'form':form})
    return redirect('/login')