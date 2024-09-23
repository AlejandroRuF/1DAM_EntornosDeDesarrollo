from funcio import check_dni
import unittest


class TestCheckDni(unittest.TestCase):
    def test_dni_correcte(self):
        resultat = check_dni("69875447K")
        self.assertEqual(resultat, True)
        resultat = check_dni("09052238J")
        self.assertEqual(resultat, True)
        resultat = check_dni("38237444J")
        self.assertEqual(resultat, True)
        resultat = check_dni("84317227D")
        self.assertEqual(resultat, True)
        resultat = check_dni("07267666B")
        self.assertEqual(resultat, True)



    def test_dni_incorrecte(self):
        resultat = check_dni("29835447R")
        self.assertEqual(resultat, False)
        resultat = check_dni("09053338I")
        self.assertEqual(resultat, False)
        resultat = check_dni("46488008X")
        self.assertEqual(resultat, False)
        resultat = check_dni("46488008")
        self.assertEqual(resultat, False)
        resultat = check_dni("464880085855X")
        self.assertEqual(resultat, False)
        resultat = check_dni("X46488008")
        self.assertEqual(resultat, False)
        resultat = check_dni("46488X008X")
        self.assertEqual(resultat, False)
        resultat = check_dni("46488X")
        self.assertEqual(resultat, False)
        resultat = check_dni("ABCDEFGSQ")
        self.assertEqual(resultat, False)



if __name__ == '__main__':
    unittest.main()
