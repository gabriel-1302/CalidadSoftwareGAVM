from django.urls import path
from . import views

app_name = 'personas_ui'

urlpatterns = [
    path('', views.persona_list, name='persona_list'),
    path('crear/', views.persona_create, name='persona_create'),
    path('editar/<str:carnet>/', views.persona_edit, name='persona_edit'),
    path('eliminar/<str:carnet>/', views.persona_delete, name='persona_delete'),
    path('detalle/<str:carnet>/', views.persona_detail, name='persona_detail'),
]