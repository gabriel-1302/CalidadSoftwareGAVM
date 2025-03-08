from django.shortcuts import render
from .forms import PuntajesForm
from .calculos import (
    calcular_puntajes,
    actualizacion_academica,
    experiencia_profesional,
    produccionIntelectual  # Asegúrate de importar la nueva función
)

def calcular_puntajes_view(request):
    resultados = None
    total_puntajes = 0  # Inicializar total_puntajes
    if request.method == 'POST':
        form = PuntajesForm(request.POST)
        if form.is_valid():
            # Sección A - Formación Académica
            datos_formacion = {
                'diplomados': form.cleaned_data['diplomados'],
                'especialidades': form.cleaned_data['especialidades'],
                'maestrias': form.cleaned_data['maestrias'],
                'doctorados': form.cleaned_data['doctorados']
            }
            resultados_formacion = calcular_puntajes(**datos_formacion)
            
            # Sección B - Actualización Académica
            actualizacion = form.cleaned_data['actualizacion']
            puntaje_actualizacion = actualizacion_academica(actualizacion)
            subtotal_actualizacion = min(puntaje_actualizacion, 6)
            resultados_actualizacion = (puntaje_actualizacion, subtotal_actualizacion)
            
            # Sección C - Experiencia Profesional
            datos_experiencia = {
                'antiguedad': form.cleaned_data['antiguedad'],
                'publica': form.cleaned_data['publica'],
                'docente': form.cleaned_data['docente']
            }
            resultados_experiencia = experiencia_profesional(**datos_experiencia)
            
            # Sección D - Producción Intelectual (Nueva sección)
            articulos = form.cleaned_data['articulos_publicados']
            resultados_produccion = produccionIntelectual(articulos)
            
            total_puntajes = resultados_formacion[-1] + subtotal_actualizacion + resultados_experiencia[-1] + resultados_produccion[-1]

            # Combinar todos los resultados
            resultados = (
                resultados_formacion +    # Índices 0-4
                resultados_actualizacion + # Índices 5-6
                resultados_experiencia +  # Índices 7-10
                resultados_produccion     # Índices 11-12 (puntaje, subtotal)
            )
    else:
        form = PuntajesForm()
    
    return render(request, 'calculadora_puntajes/formulario.html', {
        'form': form,
        'resultados': resultados,
        'total_puntajes': total_puntajes,
    })