from django import forms

from gestionusuarios.models import Persona, Propuesta, Tipo, Term, Statuspropuesta, Trabajogrado, Statustrabajogrado

class TipoForm(forms.ModelForm):

    class Meta:
        model = Tipo

        fields = [
            'Nombretipo',
        ]
        labels = {
            'Nombretipo': 'Nombretipo',
        }
        widgets = {
            'Nombretipo': forms.TextInput(attrs={'class':'form-control'}),
        }

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'Tipousuario',
            'Cedula',
            'Nombres',
            'Apellidos',
            'Correoucab',
            'Correopersonal',
            'TelefonoPrincipal',
            'TelefonoSecundario',
            'Observaciones',
        ]
        labels = {
            'Tipousuario': 'Tipousuario',
            'Cedula': 'Cedula',
            'Nombres': 'Nombres',
            'Apellidos': 'Apellidos',
            'Correoucab': 'Correo UCAB',
            'Correopersonal': 'Correo personal',
            'TelefonoPrincipal': 'Telefono Principal',
            'TelefonoSecundario': 'Telefono Alternativo',
            'Observaciones': 'Observaciones',
        }
        widgets = {
            'Tipousuario': forms.Select(attrs={'class':'form-control'}),
            'Cedula': forms.TextInput(attrs={'class':'form-control'}),
            'Nombres': forms.TextInput(attrs={'class':'form-control'}),
            'Apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'Correoucab': forms.TextInput(attrs={'class':'form-control'}),
            'Correopersonal': forms.TextInput(attrs={'class':'form-control'}),
            'TelefonoPrincipal': forms.TextInput(attrs={'class':'form-control'}),
            'TelefonoSecundario': forms.TextInput(attrs={'class':'form-control'}),
            'Observaciones': forms.TextInput(attrs={'class':'form-control'}),
        }


class TermForm(forms.ModelForm):

    class Meta:
        model = Term

        fields = [
            'Periodo',
        ]
        labels = {
            'Periodo': 'Periodo',
        }
        widgets = {
            'Periodo': forms.TextInput(attrs={'class':'form-control'}),
        }


class StatusPropuestaForm(forms.ModelForm):

    class Meta:
        model = Statuspropuesta

        fields = [
            'Estatus',
        ]
        labels = {
            'Estatus': 'Estatus',
        }
        widgets = {
            'Estatus': forms.TextInput(attrs={'class':'form-control'}),
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class PropuestaForm(forms.ModelForm):

    class Meta:
        model = Propuesta

        fields = [
            'Estatusvalor',
            'Termpropuesta',
            'Codigo',
            'Fechaentrega',
            'Titulo',
            'Alumnouno',
            'Alumnodos',
        ]
        labels = {
            'Estatusvalor': 'Estatus de la propuesta',
            'Termpropuesta': 'TERM de la propuesta',
            'Codigo': 'Codigo',
            'Fechaentrega': 'Fecha de entrega',
            'Titulo': 'Titulo de la propuesta',
            'Alumnouno': 'Primer Alumno',
            'Alumnodos': 'Segundo Alumno',
        }
        widgets = {
            'Estatusvalor': forms.Select(attrs={'class':'form-control'}),
            'Termpropuesta': forms.Select(attrs={'class':'form-control'}),
            'Codigo': forms.TextInput(attrs={'class':'form-control'}),
            'Fechaentrega': DateInput(attrs={'class':'form-control'}),
            'Titulo': forms.TextInput(attrs={'class':'form-control'}),
            'Alumnouno': forms.Select(attrs={'class':'form-control'}),
            'Alumnodos': forms.Select(attrs={'class':'form-control'}),
        }


class StatusGradoForm(forms.ModelForm):

    class Meta:
        model = Statustrabajogrado

        fields = [
            'Estatustg',
        ]
        labels = {
            'Estatustg': 'Estatus TG',
        }
        widgets = {
            'Estatustg': forms.TextInput(attrs={'class':'form-control'}),
        }


class TrabajogradoForm(forms.ModelForm):

    class Meta:
        model = Trabajogrado

        fields = [
            'Asocpropuesta',
            'TituloTG',
            'Termtrabajogrado',
            'Estatustrabajo',
            'NRC',
            'Descriptores',
            'Categoriatem',
            'Fechaentrega',
            'Nombreempresa',
        ]
        labels = {
            'Asocpropuesta': 'Propuesta asociada',
            'TituloTG': 'Titulo TG (Diferente a propuesta)',
            'Termtrabajogrado': 'TERM',
            'Estatustrabajo': 'Estatus de TG',
            'NRC': 'NRC',
            'Descriptores': 'Descriptores',
            'Categoriatem': 'Categoría temática',
            'Fechaentrega': 'Fecha de entrega',
            'Nombreempresa': 'Nombre de la empresa',
        }
        widgets = {
            'Asocpropuesta': forms.Select(attrs={'class':'form-control'}),
            'TituloTG': forms.TextInput(attrs={'class':'form-control'}),
            'Termtrabajogrado': forms.Select(attrs={'class':'form-control'}),
            'Estatustrabajo': forms.Select(attrs={'class':'form-control'}),
            'NRC': forms.TextInput(attrs={'class':'form-control'}),
            'Descriptores': forms.TextInput(attrs={'class':'form-control'}),
            'Categoriatem': forms.TextInput(attrs={'class':'form-control'}),
            'Fechaentrega': DateInput(attrs={'class':'form-control'}),
            'Nombreempresa': forms.TextInput(attrs={'class':'form-control'}),
        }

