# Generated by Django 5.2.1 on 2025-05-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('anio', models.IntegerField()),
                ('carrera', models.CharField(max_length=100)),
            ],
        ),
    ]
