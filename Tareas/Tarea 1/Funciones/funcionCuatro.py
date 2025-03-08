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