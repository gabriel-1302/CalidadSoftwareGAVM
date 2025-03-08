import unittest
from pruebaDos import calcular_puntajes

class TestCalculoPuntajes(unittest.TestCase):
    
    def test_caso_usuario(self):
        self.assertEqual(calcular_puntajes(5, 0, 1, 0), (4, 0, 8, 0, 12))
    
    def test_especialidad_cero(self):
        self.assertEqual(calcular_puntajes(0, 0, 0, 0), (0, 0, 0, 0, 0))
        self.assertEqual(calcular_puntajes(2, 0, 1, 0), (3, 0, 8, 0, 11))
    
    def test_maestria_max(self):
        self.assertEqual(calcular_puntajes(0, 0, 3, 0), (0, 0, 11, 0, 11))
    
    def test_doctorado_prioridad(self):
        self.assertEqual(calcular_puntajes(10, 10, 10, 1), (0, 0, 0, 12, 12))

if __name__ == '__main__':
    unittest.main()