def calcular_puntajes(diplomados, especialidades, maestrias, doctorados):
    # Cálculo puntaje diplomados
    if diplomados <= 0:
        puntaje_diplomados = 0
    else:
        puntaje_diplomados = min(1 + diplomados, 4)  # 2 + (n-1) con máximo 4
    
    # Cálculo puntaje especialidades
    if especialidades <= 0:
        puntaje_especialidades = 0
    else:
        puntaje_especialidades = min(2 * (1 + especialidades), 6)  # 4 + 2(n-1) con máximo 6
    
    # Cálculo puntaje maestrías
    if maestrias <= 0:
        puntaje_maestrias = 0
    else:
        puntaje_maestrias = min(5 + 3 * maestrias, 11)  # 8 + 3(n-1) con máximo 11
    
    # Cálculo puntaje doctorados
    puntaje_doctorados = min(12 * doctorados, 12)  # Máximo 12
    
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


total=calcular_puntajes(5,89,1,2)
print(total)