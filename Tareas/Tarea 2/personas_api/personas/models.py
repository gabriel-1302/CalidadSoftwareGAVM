from django.db import models

# Create your models here.
from django.db import models

class Persona(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    carnet = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    direccion = models.TextField()
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"