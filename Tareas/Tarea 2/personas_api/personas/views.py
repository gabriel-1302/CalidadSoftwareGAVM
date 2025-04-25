from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerializer



class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filterset_fields = ['carnet', 'nombres', 'apellidos']