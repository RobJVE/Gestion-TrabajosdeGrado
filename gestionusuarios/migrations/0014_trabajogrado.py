# Generated by Django 2.2.7 on 2020-01-06 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionusuarios', '0013_statustrabajogrado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajogrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TituloTG', models.CharField(blank=True, max_length=60)),
                ('NRC', models.CharField(max_length=12, unique=True)),
                ('Descriptores', models.CharField(max_length=50)),
                ('Categoriatem', models.CharField(max_length=50)),
                ('Fechaentrega', models.DateField()),
                ('Nombreempresa', models.CharField(max_length=50)),
                ('Asocpropuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionusuarios.Propuesta')),
                ('Termtrabajogrado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionusuarios.Term')),
            ],
        ),
    ]
