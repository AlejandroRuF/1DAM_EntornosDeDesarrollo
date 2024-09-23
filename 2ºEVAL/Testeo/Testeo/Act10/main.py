import unittest

from funcion import bisiesto

class Test_anyo(unittest.TestCase):
    def test_fechaok(self):
        resultat = bisiesto(1992)
        self.assertEqual(resultat, True)
        resultat = bisiesto(2000)
        self.assertEqual(resultat, True)
        resultat = bisiesto(2012)
        self.assertEqual(resultat, True)
        resultat = bisiesto(1972)
        self.assertEqual(resultat, True)
        resultat = bisiesto(2160)
        self.assertEqual(resultat, True)
        resultat = bisiesto(2048)
        self.assertEqual(resultat, True)

    def test_fechaFalse(self):
        resultat = bisiesto(2200)
        self.assertEqual(resultat, False)
        resultat = bisiesto(1993)
        self.assertEqual(resultat, False)
        resultat = bisiesto(1994)
        self.assertEqual(resultat, False)
        resultat = bisiesto(2103)
        self.assertEqual(resultat, False)
        resultat = bisiesto(1914)
        self.assertEqual(resultat, False)


if __name__ == '__main__':
    unittest.main()