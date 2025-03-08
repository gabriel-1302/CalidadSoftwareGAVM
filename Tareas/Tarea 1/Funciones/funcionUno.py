def calcular_puntajes(diplomados, especialidades, maestrias, doctorados):
    # Cálculo puntaje diplomados
    if diplomados <= 0:
        puntaje_diplomados = 0
    else:
        puntaje_diplomados = 1 + diplomados  # Equivalente a 2 + (n - 1)
    
    # Cálculo puntaje especialidades
    if especialidades <= 0:
        puntaje_especialidades = 0
    else:
        puntaje_especialidades = 2 * (1 + especialidades)  # Equivalente a 4 + 2*(n - 1)
    
    # Cálculo puntaje maestrías
    if maestrias <= 0:
        puntaje_maestrias = 0
    else:
        puntaje_maestrias = 5 + 3 * maestrias  # Equivalente a 8 + 3*(n - 1)
    
    # Cálculo puntaje doctorados
    puntaje_doctorados = 12 * doctorados
    
    # Cálculo del subtotal
    subtotal = (
        puntaje_diplomados 
        + puntaje_especialidades 
        + puntaje_maestrias 
        + puntaje_doctorados
    )
    
    return (
        puntaje_diplomados,
        puntaje_especialidades,
        puntaje_maestrias,
        puntaje_doctorados,
        subtotal
    )




