# Generated by Django 2.2.7 on 2019-12-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionusuarios', '0004_auto_20191218_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statuspropuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estatus', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Periodo', models.IntegerField()),
            ],
        ),
    ]
