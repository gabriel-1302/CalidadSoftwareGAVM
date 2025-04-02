import unittest
from funciones import calcular_area_circulo
import math


class TestCalcularAreaCirculo(unittest.TestCase):
    
    def test_radioPositivo(self):
        """Prueba con radio positivo (r=5)"""
        resultado = calcular_area_circulo(5)
        self.assertAlmostEqual(resultado, math.pi * 25, places=5)
    
    def test_radioCero(self):
        """Prueba con radio cero (r=0)"""
        resultado = calcular_area_circulo(0)
        self.assertEqual(resultado, 0)
    
    def test_radioNegativo(self):
        """Prueba con radio negativo (r=-3) - debe lanzar excepción"""
        with self.assertRaises(ValueError):
            calcular_area_circulo(-3)
    
    def test_radioGrande(self):
        """Prueba con radio grande (r=100)"""
        resultado = calcular_area_circulo(100)
        self.assertAlmostEqual(resultado, math.pi * 10000, places=5)
    
    def test_radioDecimal(self):
        """Prueba con radio decimal (r=3.5)"""
        resultado = calcular_area_circulo(3.5)
        self.assertAlmostEqual(resultado, math.pi * 12.25, places=5)

if __name__ == '__main__':
    unittest.main()