import math


def calcular_area_circulo(radio):
    if radio < -1:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radio ** 2



def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    max_divisor = math.isqrt(n) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True