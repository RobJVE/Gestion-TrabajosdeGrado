# Generated by Django 2.2.7 on 2019-12-18 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cedula', models.CharField(max_length=9)),
                ('Nombres', models.CharField(max_length=40)),
                ('Apellidos', models.CharField(max_length=40)),
                ('Correoucab', models.CharField(max_length=30)),
                ('Correopersonal', models.CharField(max_length=30)),
                ('TelefonoPrincipal', models.CharField(max_length=11)),
                ('TelefonoSecundario', models.CharField(max_length=11)),
                ('Observaciones', models.CharField(max_length=200)),
                ('Tipo', models.CharField(choices=[('Profesor', 'Profesor'), ('Alumno', 'Alumno')], default='Profesor', max_length=15)),
            ],
        ),
    ]
