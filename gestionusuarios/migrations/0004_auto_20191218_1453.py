# Generated by Django 2.2.7 on 2019-12-18 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionusuarios', '0003_auto_20191218_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='persona',
            new_name='Tipousuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Tipo',
        ),
    ]
