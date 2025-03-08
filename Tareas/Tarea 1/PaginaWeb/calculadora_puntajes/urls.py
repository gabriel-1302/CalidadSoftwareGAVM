from django.urls import path
from . import views

app_name = 'calculadora_puntajes'
urlpatterns = [
    path('', views.calcular_puntajes_view, name='formulario'),  # URL raíz de la app
]