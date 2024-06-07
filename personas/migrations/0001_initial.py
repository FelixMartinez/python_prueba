# Generated by Django 5.0.6 on 2024-06-06 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('altura', models.FloatField()),
                ('peso', models.FloatField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
                ('tipo_documento', models.CharField(choices=[('DNI', 'DNI'), ('Pasaporte', 'Pasaporte'), ('Carnet de Extranjería', 'Carnet de Extranjería')], max_length=21)),
                ('numero_documento', models.CharField(max_length=20, unique=True)),
                ('anio_nacimiento', models.PositiveIntegerField(editable=False)),
            ],
        ),
    ]