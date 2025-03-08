def calcular_puntajes(diplomados, especialidades, maestrias, doctorados):
    subtotal = 0
    puntajes = [0, 0, 0, 0]  # [Diplomados, Especialidad, Maestría, Doctorado]
    
    # Jerarquía: Doctorado -> Maestría -> Especialidad -> Diplomado
    # Doctorado
    doctorado_p = min(12 * doctorados, 12)
    add = min(doctorado_p, 12 - subtotal)
    puntajes[3] = add
    subtotal += add
    
    if subtotal < 12:
        # Maestría
        if maestrias <= 0:
            maestria_p = 0
        else:
            maestria_p = min(8 + 3*(maestrias - 1), 11)
        add = min(maestria_p, 12 - subtotal)
        puntajes[2] = add
        subtotal += add
        
        if subtotal < 12:
            # Especialidad
            if especialidades <= 0:
                especialidad_p = 0
            else:
                especialidad_p = min(4 + 2*(especialidades - 1), 6)
            add = min(especialidad_p, 12 - subtotal)
            puntajes[1] = add
            subtotal += add
            
            if subtotal < 12:
                # Diplomado
                if diplomados <= 0:
                    diplomado_p = 0
                else:
                    diplomado_p = min(2 + 1*(diplomados - 1), 4)
                add = min(diplomado_p, 12 - subtotal)
                puntajes[0] = add
                subtotal += add
    
    return (
        puntajes[0],  # Diplomado
        puntajes[1],  # Especialidad
        puntajes[2],  # Maestría
        puntajes[3],  # Doctorado
        min(subtotal, 12)  # Subtotal
    )


def actualizacion_academica(valor: int) -> float:
    """
    Calcula la actualización académica con un máximo de 6 puntos
    Reglas:
    - Multiplica el valor de entrada por 0.5
    - Si el resultado es mayor a 6, retorna 6
    - El valor de entrada debe ser mayor a 0
    """
    if not isinstance(valor, int) or valor < 0:
        raise ValueError("El valor debe ser un entero mayor a cero")
    
    calculo = valor * 0.5
    return min(calculo, 6)




def experiencia_profesional(antiguedad: int, publica: int, docente: int) -> tuple:
    """
    Calcula los puntajes de experiencia profesional con límites establecidos
    
    Parámetros:
    antiguedad (int): Años como abogado (máximo 4)
    publica (int): Años en sector público (máximo 4)
    docente (int): Años como docente (máximo 2 puntos)
    
    Retorna:
    tuple: (p_antiguedad, p_publica, p_docente, subtotal)
    """
    
    # Validación de entradas
    if not all(isinstance(x, int) for x in [antiguedad, publica, docente]):
        raise ValueError("Todos los valores deben ser enteros")
    
    if any(x < 0 for x in [antiguedad, publica, docente]):
        raise ValueError("Los valores no pueden ser negativos")
    
    # Cálculo de puntajes individuales
    p_antiguedad = min(antiguedad, 4)
    p_publica = min(publica, 4)
    p_docente = min(docente * 2, 2)  # Máximo 2 puntos
    
    # Cálculo del subtotal
    subtotal = p_antiguedad + p_publica + p_docente
    
    return (
        p_antiguedad,
        p_publica,
        p_docente,
        min(subtotal, 10)
    )


def produccionIntelectual(articulos_publicados: int) -> tuple:
    """
    Calcula los puntos de producción intelectual con un máximo de 2 puntos
    
    Parámetros:
    articulos_publicados (int): Cantidad de artículos publicados
    
    Retorna:
    tuple: (puntaje, subtotal)
    """
    if not isinstance(articulos_publicados, int) or articulos_publicados < 0:
        raise ValueError("La cantidad de artículos debe ser un entero mayor o igual a cero")
    
    puntaje = min(articulos_publicados, 2)
    return (puntaje, puntaje)