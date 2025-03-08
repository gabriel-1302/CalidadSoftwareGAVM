import unittest

class TestProduccionIntelectual(unittest.TestCase):
    
    def test_valores_normales(self):
        self.assertEqual(produccionIntelectual(1), (1, 1))
        self.assertEqual(produccionIntelectual(2), (2, 2))
    
    def test_limite_maximo(self):
        self.assertEqual(produccionIntelectual(3), (2, 2))
        self.assertEqual(produccionIntelectual(5), (2, 2))
    
    def test_valor_cero(self):
        self.assertEqual(produccionIntelectual(0), (0, 0))
    
    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            produccionIntelectual(-1)
        
        with self.assertRaises(ValueError):
            produccionIntelectual(2.5)

if __name__ == '__main__':
    unittest.main()