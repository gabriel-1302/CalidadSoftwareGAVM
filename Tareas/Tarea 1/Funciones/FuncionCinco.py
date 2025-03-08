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