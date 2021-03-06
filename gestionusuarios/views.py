from django.shortcuts import render, redirect
from django.http import HttpResponse
from gestionusuarios.forms import UsuarioForm, PropuestaForm, TipoForm, TermForm, StatusPropuestaForm, TrabajogradoForm, StatusGradoForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .models import *

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'gestionusuarios/home.html')
    return redirect('/login')


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "gestionusuarios/login.html", {'form': form})


def logout(request):
    do_logout(request)
    return redirect('/')


def tipo_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TipoForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = TipoForm()

        return render(request, 'gestionusuarios/nuevotipopersona.html', {'form':form})
    return redirect('/login')


def usuario_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = UsuarioForm()

        return render(request, 'gestionusuarios/nuevapersona.html', {'form':form})
    return redirect('/login')


def term_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TermForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = TermForm()

        return render(request, 'gestionusuarios/nuevoterm.html', {'form':form})
    return redirect('/login')


def statuspropuesta_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = StatusPropuestaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = StatusPropuestaForm()

        return render(request, 'gestionusuarios/nuevostatuspropuesta.html', {'form':form})
    return redirect('/login')


def propuesta_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PropuestaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = PropuestaForm()

        return render(request, 'gestionusuarios/nuevapropuesta.html', {'form':form})
    return redirect('/login')


def trabajogrado_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TrabajogradoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = TrabajogradoForm()

        return render(request, 'gestionusuarios/nuevotrabajogrado.html', {'form':form})
    return redirect('/login')


def statusgrado_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = StatusGradoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = StatusGradoForm()

        return render(request, 'gestionusuarios/nuevostatusgrado.html', {'form':form})
    return redirect('/login')


def consultar_persona(request):
    if request.user.is_authenticated:
        personas = Persona.objects.order_by("Cedula")
        return render(request, "gestionusuarios/consultarpersona.html", {'personas': personas})
    return redirect('/login')


def consultar_cedula(request):
    if request.user.is_authenticated:
        buscar = request.POST['cedula']
        personas = Persona.objects.filter(Cedula=buscar)
        return render(request, "gestionusuarios/consultarcedula.html", {'personas': personas})
    return redirect('/login')


def consultar_nombre(request):
    if request.user.is_authenticated:
        buscar = request.POST['nombres']
        personas = Persona.objects.filter(Nombres=buscar)
        return render(request, "gestionusuarios/consultarnombre.html", {'personas': personas})
    return redirect('/login')


def consultar_term(request):
    if request.user.is_authenticated:
        terms = Term.objects.all()
        return render(request, "gestionusuarios/consultaterm.html", {'terms': terms})
    return redirect('/login')


def consultar_tipopersona(request):
    if request.user.is_authenticated:
        tipos = Tipo.objects.all()
        return render(request, "gestionusuarios/consultartipopersona.html", {'tipos': tipos})
    return redirect('/login')


def consultar_propuesta(request):
    if request.user.is_authenticated:
        propuestas = Propuesta.objects.all()
        return render(request, "gestionusuarios/consultarpropuesta.html", {'propuestas': propuestas})
    return redirect('/login')


def consultar_statuspropuesta(request):
    if request.user.is_authenticated:
        statuspropuestas = Statuspropuesta.objects.all()
        return render(request, "gestionusuarios/consultarstatuspropuesta.html", {'statuspropuestas': statuspropuestas})
    return redirect('/login')


def consultar_propuestaaprobada(request):
    if request.user.is_authenticated:
        propaprobadas = Propuesta.objects.filter(Estatusvalor__Estatus='Aprobada')
        return render(request, "gestionusuarios/consultarpropuestaaprobada.html", {'propaprobadas': propaprobadas})
    return redirect('/login')


def consultar_trabajogrado(request):
    if request.user.is_authenticated:
        trabajos = Trabajogrado.objects.all()
        return render(request, "gestionusuarios/consultatrabajogrado.html", {'trabajos': trabajos})
    return redirect('/login')


def consultar_statusgrado(request):
    if request.user.is_authenticated:
        statustg = Statustrabajogrado.objects.all()
        return render(request, "gestionusuarios/consultastatusgrado.html", {'statustg': statustg})
    return redirect('/login')


def editar_persona(request, idpersona):
    if request.user.is_authenticated:
        p = Persona.objects.get(Cedula=idpersona)
        if request.method == 'GET':
            form = UsuarioForm(instance=p)
        else:
            form = UsuarioForm(request.POST, instance=p)
            if form.is_valid():
                form.save()
            return redirect('/consultarpersona')
        return render(request, "gestionusuarios/nuevapersona.html", {'form': form})
    return redirect('/login')


def editar_term(request, periodo):
    if request.user.is_authenticated:
        p = Term.objects.get(Periodo=periodo)
        if request.method == 'GET':
            form = TermForm(instance=p)
        else:
            form = TermForm(request.POST, instance=p)
            if form.is_valid():
                form.save()
            return redirect('/consultaterm')
        return render(request, "gestionusuarios/nuevoterm.html", {'form': form})
    return redirect('/login')


def editar_tipopersona(request, id):
    if request.user.is_authenticated:
        p = Tipo.objects.get(id=id)
        if request.method == 'GET':
            form = TipoForm(instance=p)
        else:
            form = TipoForm(request.POST, instance=p)
            if form.is_valid():
                form.save()
            return redirect('/consultatipopersona')
        return render(request, "gestionusuarios/nuevotipopersona.html", {'form': form})
    return redirect('/login')


def editar_propuesta(request, id):
    if request.user.is_authenticated:
        p = Propuesta.objects.get(id=id)
        if request.method == 'GET':
            form = PropuestaForm(instance=p)
        else:
            form = PropuestaForm(request.POST, instance=p)
            if form.is_valid():
                form.save()
            return redirect('/consultarpropuesta')
        return render(request, "gestionusuarios/nuevapropuesta.html", {'form': form})
    return redirect('/login')


def editar_estatusprop(request, id):
    if request.user.is_authenticated:
        p = Statuspropuesta.objects.get(id=id)
        if request.method == 'GET':
            form = StatusPropuestaForm(instance=p)
        else:
            form = StatusPropuestaForm(request.POST, instance=p)
            if form.is_valid():
                form.save()
            return redirect('/consultarstatuspropuesta')
        return render(request, "gestionusuarios/nuevostatuspropuesta.html", {'form': form})
    return redirect('/login')