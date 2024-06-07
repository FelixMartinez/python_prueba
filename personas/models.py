from django.db import models
from datetime import date

class Persona(models.Model):
  SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
  ]

  DOCUMENTO_CHOICES = [
    ('DNI', 'DNI'),
    ('Pasaporte', 'Pasaporte'),
    ('Carnet de Extranjería', 'Carnet de Extranjería'),
  ]

  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  edad = models.PositiveIntegerField()
  altura = models.FloatField()
  peso = models.FloatField()
  sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
  tipo_documento = models.CharField(max_length=21, choices=DOCUMENTO_CHOICES)
  numero_documento = models.CharField(max_length=20, unique=True)
  anio_nacimiento = models.PositiveIntegerField(editable=False)

  def save(self, *args, **kwargs):
    from datetime import date
    self.anio_nacimiento = date.today().year - self.edad
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.nombre} {self.apellido}"