from django.shortcuts import render
from django.http import HttpResponse

from gestionusuarios.forms import UsuarioForm, PropuestaForm

# Create your views here.

def index(request):
    return render(request, 'gestionusuarios/home.html')


def usuario_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()

    return render(request, 'gestionusuarios/index.html', {'form':form})


def propuesta_view(request):
    if request.method == 'POST':
        form = PropuestaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PropuestaForm()

    return render(request, 'gestionusuarios/indexreplica.html', {'form':form})