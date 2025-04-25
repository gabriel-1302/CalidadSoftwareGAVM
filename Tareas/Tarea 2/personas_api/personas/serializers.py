from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'carnet', 'nombres', 'apellidos', 'sexo', 
                 'fecha_nacimiento', 'profesion', 'celular', 'direccion']