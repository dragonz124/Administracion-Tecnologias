import unittest
from funciones import sumar


class TestSumar(unittest.TestCase):

    def test_sumar_positivos(self):
        resultado = sumar(2, 3)
        self.assertEqual(resultado, 6)

    def test_sumar_negativos(self):
        resultado = sumar(2, -5)
        self.assertEqual(resultado, -3)

    def test_sumar_cero(self):
        resultado = sumar(0, 0)
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()
