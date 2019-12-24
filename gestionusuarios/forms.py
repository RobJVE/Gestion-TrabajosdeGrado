from django import forms

from gestionusuarios.models import Usuario, Propuesta

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario

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


class PropuestaForm(forms.ModelForm):

    class Meta:
        model = Propuesta

        fields = [
            'Estatusvalor',
            'Codigo',
            'Fechaentrega',
            'Titulo',
        ]
        labels = {
            'Estatusvalor': 'Estatus de la propuesta',
            'Codigo': 'Codigo',
            'Fechaentrega': 'Fecha de entrega',
            'Titulo': 'Titulo de la propuesta',
        }
        widgets = {
            'Estatusvalor': forms.Select(attrs={'class':'form-control'}),
            'Codigo': forms.TextInput(attrs={'class':'form-control'}),
            'Fechaentrega': forms.DateInput(attrs={'class':'form-control'}),
            'Titulo': forms.TextInput(attrs={'class':'form-control'}),
        }