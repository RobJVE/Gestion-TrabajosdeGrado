from django.db import models

# Create your models here.

class Tipo(models.Model):
    Nombretipo = models.CharField(max_length=14)

    def __str__(self):
        return self.Nombretipo


class Persona(models.Model):
    Tipousuario = models.ForeignKey(Tipo, null=True, on_delete=models.CASCADE)
    Cedula = models.CharField(unique=True, max_length=9)
    Nombres = models.CharField(max_length=40)
    Apellidos = models.CharField(max_length=40)
    Correoucab = models.CharField(blank=True, max_length=45)
    Correopersonal = models.CharField(max_length=45)
    TelefonoPrincipal = models.CharField(max_length=11)
    TelefonoSecundario = models.CharField(max_length=11)
    Observaciones = models.CharField(max_length=200)

    def __str__(self):
        return self.Nombres + ' ' + self.Apellidos


class Term(models.Model):
    Periodo = models.IntegerField()

    def __str__(self):
        return str(self.Periodo)


class Statuspropuesta(models.Model):
    Estatus = models.CharField(max_length=14)

    def __str__(self):
        return self.Estatus
        

class Propuesta(models.Model):
    Estatusvalor = models.ForeignKey(Statuspropuesta, on_delete=models.CASCADE)
    Termpropuesta = models.ForeignKey(Term, null=True, on_delete=models.CASCADE)
    Fechaentrega = models.DateField()
    Codigo = models.CharField(unique=True, max_length=12)
    Titulo = models.CharField(max_length=60)
    Alumnouno = models.ForeignKey(Persona, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Titulo


        


