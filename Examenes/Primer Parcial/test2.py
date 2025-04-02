import math
import unittest
from funciones import es_primo

class TestEsPrimo(unittest.TestCase):
    
    def test_numeroPrimo(self):
        """Prueba con número primo (n=7)"""
        self.assertTrue(es_primo(7))
    
    def test_numeroNoPrimo(self):
        """Prueba con número no primo (n=6)"""
        self.assertFalse(es_primo(6))
    
    def test_numeroNegativo(self):
        """Prueba con número negativo (n=-3)"""
        self.assertFalse(es_primo(-3))
    
    def test_numeroGrande(self):
        """Prueba con número grande primo (n=997)"""
        self.assertTrue(es_primo(997))
    
    def test_numeroCero(self):
        """Prueba con cero (n=0)"""
        self.assertFalse(es_primo(0))

if __name__ == '__main__':
    unittest.main()