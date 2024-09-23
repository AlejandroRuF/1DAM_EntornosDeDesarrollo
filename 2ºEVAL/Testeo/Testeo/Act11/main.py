import unittest

from funcion import segle21


class test_siglo21(unittest.TestCase):

    def test_fecha_correcta(self):
        resultado = segle21(1, 1, 2023)
        self.assertEqual(resultado, True)
        resultado = segle21(1, 2, 2023)
        self.assertEqual(resultado, True)
        resultado = segle21(1, 3, 2002)
        self.assertEqual(resultado, True)
        resultado = segle21(21, 5, 2035)
        self.assertEqual(resultado, True)

    def test_fecha_incorrecta(self):
        resultado = segle21(1, 1, 1000)
        self.assertEqual(resultado, False)
        resultado = segle21(1, 13, 2005)
        self.assertEqual(resultado, False)
        resultado = segle21(141, 5, 2005)
        self.assertEqual(resultado, False)
        resultado = segle21(31, 4, 2005)
        self.assertEqual(resultado, False)
        resultado = segle21(30, 2, 2004)
        self.assertEqual(resultado, False)
        resultado = segle21(29, 2, 2005)
        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()
