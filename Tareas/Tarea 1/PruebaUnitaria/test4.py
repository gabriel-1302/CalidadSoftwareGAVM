import unittest
from funcion import experiencia_profesional
class TestExperienciaProfesional(unittest.TestCase):
    
    def test_valores_normales(self):
        self.assertEqual(experiencia_profesional(3, 2, 1), (3, 2, 2, 7))
    
    def test_limites_maximos(self):
        self.assertEqual(experiencia_profesional(5, 5, 2), (4, 4, 2, 10))
    
    def test_sobrepasa_subtotal(self):
        self.assertEqual(experiencia_profesional(4, 4, 1), (4, 4, 2, 10))
    
    def test_valores_cero(self):
        self.assertEqual(experiencia_profesional(0, 0, 0), (0, 0, 0, 0))
    
    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            experiencia_profesional(-1, 2, 3)
        
        with self.assertRaises(ValueError):
            experiencia_profesional(3.5, 2, 1)

if __name__ == '__main__':
    unittest.main()