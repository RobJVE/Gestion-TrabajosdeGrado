# Generated by Django 2.2.7 on 2020-01-06 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionusuarios', '0011_auto_20200106_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='propuesta',
            name='Alumnodos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Alumnodos', to='gestionusuarios.Persona'),
        ),
        migrations.AlterField(
            model_name='propuesta',
            name='Alumnouno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Alumnouno', to='gestionusuarios.Persona'),
        ),
    ]
