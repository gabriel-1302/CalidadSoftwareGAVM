from django.shortcuts import render

# Create your views here.
import requests
import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
API_URL = settings.API_BASE_URL + 'personas/'

def persona_list(request):
    """Vista para listar todas las personas"""
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            personas = response.json()
            return render(request, 'personas_ui/list.html', {'personas': personas})
        else:
            messages.error(request, f"Error al obtener datos: {response.status_code}")
            return render(request, 'personas_ui/list.html', {'personas': []})
    except Exception as e:
        messages.error(request, f"Error de conexión: {str(e)}")
        return render(request, 'personas_ui/list.html', {'personas': []})

def persona_detail(request, carnet):
    """Vista para ver detalles de una persona"""
    try:
        # Primero obtenemos todas las personas y filtramos por carnet
        response = requests.get(API_URL)
        if response.status_code == 200:
            todas_personas = response.json()
            persona = next((p for p in todas_personas if p['carnet'] == carnet), None)
            
            if persona:
                # Formatear fecha para mostrar más legible
                fecha = datetime.strptime(persona['fecha_nacimiento'], '%Y-%m-%d')
                persona['fecha_formato'] = fecha.strftime('%d/%m/%Y')
                
                return render(request, 'personas_ui/detail.html', {'persona': persona})
        
        raise Http404("Persona no encontrada")
    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect('personas_ui:persona_list')
@csrf_exempt
def persona_create(request):
    """Vista para crear una nueva persona"""
    if request.method == 'POST':
        # Recopilar datos del formulario
        nueva_persona = {
            'carnet': request.POST.get('carnet'),
            'nombres': request.POST.get('nombres'),
            'apellidos': request.POST.get('apellidos'),
            'sexo': request.POST.get('sexo'),
            'fecha_nacimiento': request.POST.get('fecha_nacimiento'),
            'profesion': request.POST.get('profesion'),
            'celular': request.POST.get('celular'),
            'direccion': request.POST.get('direccion')
        }
        
        # Enviar datos a la API
        try:
            response = requests.post(
                API_URL,
                data=json.dumps(nueva_persona),
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 201:  # Created
                messages.success(request, "Persona creada exitosamente")
                return redirect('personas_ui:persona_list')
            else:
                messages.error(request, f"Error al crear: {response.text}")
        except Exception as e:
            messages.error(request, f"Error de conexión: {str(e)}")
    
    # GET request - mostrar formulario
    return render(request, 'personas_ui/create.html')

def persona_edit(request, carnet):
    """Vista para editar una persona existente"""
    # Primero buscamos la persona por su carnet
    try:
        response = requests.get(API_URL)
        todas_personas = response.json()
        persona = next((p for p in todas_personas if p['carnet'] == carnet), None)
        
        if not persona:
            raise Http404("Persona no encontrada")
        
        if request.method == 'POST':
            # Recopilar datos actualizados
            persona_actualizada = {
                'id': persona['id'],
                'carnet': request.POST.get('carnet'),
                'nombres': request.POST.get('nombres'),
                'apellidos': request.POST.get('apellidos'),
                'sexo': request.POST.get('sexo'),
                'fecha_nacimiento': request.POST.get('fecha_nacimiento'),
                'profesion': request.POST.get('profesion'),
                'celular': request.POST.get('celular'),
                'direccion': request.POST.get('direccion')
            }
            
            # Enviar actualización a la API
            response = requests.put(
                f"{API_URL}{persona['id']}/",
                data=json.dumps(persona_actualizada),
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                messages.success(request, "Información actualizada correctamente")
                return redirect('personas_ui:persona_list')
            else:
                messages.error(request, f"Error al actualizar: {response.text}")
        
        # GET request - mostrar formulario con datos
        return render(request, 'personas_ui/edit.html', {'persona': persona})
    
    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect('personas_ui:persona_list')

def persona_delete(request, carnet):
    """Vista para eliminar una persona"""
    try:
        # Primero obtenemos el ID de la persona a partir del carnet
        response = requests.get(API_URL)
        todas_personas = response.json()
        persona = next((p for p in todas_personas if p['carnet'] == carnet), None)
        
        if not persona:
            raise Http404("Persona no encontrada")
        
        if request.method == 'POST':
            # Confirmar eliminación
            response = requests.delete(f"{API_URL}{persona['id']}/")
            
            if response.status_code == 204:  # No Content
                messages.success(request, "Persona eliminada correctamente")
            else:
                messages.error(request, f"Error al eliminar: {response.status_code}")
            
            return redirect('personas_ui:persona_list')
        
        # GET request - mostrar confirmación
        return render(request, 'personas_ui/delete.html', {'persona': persona})
    
    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect('personas_ui:persona_list')
