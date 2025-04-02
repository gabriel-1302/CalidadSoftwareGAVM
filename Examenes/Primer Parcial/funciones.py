import math


def calcular_area_circulo(radio):
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radio ** 3



