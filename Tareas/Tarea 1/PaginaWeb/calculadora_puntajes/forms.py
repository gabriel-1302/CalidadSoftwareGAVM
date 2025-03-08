from django import forms

class PuntajesForm(forms.Form):
    # Sección A - Formación Académica
    diplomados = forms.IntegerField(
        label='Diplomados',
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'title': 'Número de diplomados obtenidos'
        })
    )
    
    especialidades = forms.IntegerField(
        label='Especialidades',
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'title': 'Número de especialidades realizadas'
        })
    )
    
    maestrias = forms.IntegerField(
        label='Maestrías',
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'title': 'Número de maestrías completadas'
        })
    )
    
    doctorados = forms.IntegerField(
        label='Doctorados',
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'title': 'Número de doctorados obtenidos'
        })
    )

    # Sección B - Actualización Académica
    actualizacion = forms.IntegerField(
        label='Eventos de actualización',
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'title': 'Número de eventos académicos asistidos'
        })
    )

    # Sección C - Experiencia Profesional
    antiguedad = forms.IntegerField(
        label='Años como abogado',
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'title': 'Años de experiencia como abogado'
        })
    )
    
    publica = forms.IntegerField(
        label='Años en sector público',
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'title': 'Años de experiencia en sector público'
        })
    )
    
    docente = forms.IntegerField(
        label='Años como docente',
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'title': 'Años de experiencia docente universitaria'
        })
    )

    articulos_publicados = forms.IntegerField(
        label='Artículos publicados',
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'title': 'Número de artículos académicos publicados'
        })
    )