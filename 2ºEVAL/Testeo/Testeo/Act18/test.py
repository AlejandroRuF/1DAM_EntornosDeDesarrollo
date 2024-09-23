import unittest

from contrasenya import Contrasenya

class Test_Contrasenya(unittest.TestCase):
    def test_crear_Contrasenya(self):
        c1 = Contrasenya("Abc$$123degh1$BAAA", 10, 2, 2, 1, 1)
        print(c1)

    def test_getters_y_setersOK(self):
        c1 = Contrasenya("Abc12_", 5, 1, 1, 1, 1)

        self.assertEqual(c1.get_simbolos(), 1)
        self.assertEqual(c1.get_nums(), 1)
        self.assertEqual(c1.get_mayus(), 1)
        self.assertEqual(c1.get_minus(), 1)
        self.assertEqual(c1.get_longitud(), 5)
        self.assertEqual(c1.get_contrasena(), "Abc12_")

        self.assertEqual(c1.set_simbolos(2), None)
        self.assertEqual(c1.set_nums(2), None)
        self.assertEqual(c1.set_mayus(2), None)
        self.assertEqual(c1.set_minus(2), None)
        self.assertEqual(c1.set_longitud(10), None)
        self.assertEqual(c1.set_contrasena("Abc12_Abc12_"), None)


        self.assertEqual(c1.get_simbolos(), 2)
        self.assertEqual(c1.get_nums(), 2)
        self.assertEqual(c1.get_mayus(), 2)
        self.assertEqual(c1.get_minus(), 2)
        self.assertEqual(c1.get_longitud(), 10)
        self.assertEqual(c1.get_contrasena(), "Abc12_Abc12_")

    def test_settersERROR(self):
        c1 = Contrasenya("Abc12_", 5, 1, 1, 1, 1)

        with self.assertRaises(Exception) as cm:
            c1.set_simbolos("2")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de símbolos debe de ser un entero")
        with self.assertRaises(Exception) as cm:
            c1.set_simbolos(-2)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de símbolos tiene que ser mayor o igual que cero")

        with self.assertRaises(Exception) as cm:
            c1.set_nums("2")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de números debe de ser un entero")
        with self.assertRaises(Exception) as cm:
            c1.set_nums(-2)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de números tiene que ser mayor o igual que cero")

        with self.assertRaises(Exception) as cm:
            c1.set_mayus("2")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de mayúsculas debe de ser un entero")
        with self.assertRaises(Exception) as cm:
            c1.set_mayus(-2)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de mayúsculas tiene que ser mayor o igual que cero")

        with self.assertRaises(Exception) as cm:
            c1.set_minus("2")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de minúsculas debe de ser un entero")
        with self.assertRaises(Exception) as cm:
            c1.set_minus(-2)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de minúsculas tiene que ser mayor o igual que cero")

        with self.assertRaises(Exception) as cm:
            c1.set_longitud("2")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La longitud debe de ser un entero")
        with self.assertRaises(Exception) as cm:
            c1.set_longitud(-2)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La longitud de la contraseña tiene que ser un número positivo")
        with self.assertRaises(Exception) as cm:
            c1.set_longitud(1)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La longitud mínima de la contraseña no cumple requisitos")

        with self.assertRaises(Exception) as cm:
            c1.set_contrasena(1235)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La contraseña debe de ser una cadena")
        with self.assertRaises(Exception) as cm:
            c1.set_contrasena("")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La contraseña no puede estar vacía")


    def test_check_contrasenaOK(self):
        c1 = Contrasenya("Abc$$123degh1$BAAA", 10, 2, 2, 1, 1)
        self.assertEqual(c1.check_contrasena(), None)

    def test_check_contrasenaERROR(self):
        c1 = Contrasenya("Abc$$123degh1$BAAA", 10, 2, 2, 1, 1)

        with self.assertRaises(Exception) as cm:
            c1.set_contrasena("123")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La contraseña no tiene la lontigud mínima indicada")

        with self.assertRaises(Exception) as cm:
            c1.set_contrasena("1234567890")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La contraseña no tiene el número mínimo de minúsculas indicados")

        with self.assertRaises(Exception) as cm:
            c1.set_contrasena("1234567890asdfg")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La contraseña no tiene el número mínimo de mayúsculas indicados")

        with self.assertRaises(Exception) as cm:
            c1.set_contrasena("ASDFGHJKLasdfg")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La contraseña no tiene el número mínimo de números indicados")

        with self.assertRaises(Exception) as cm:
            c1.set_contrasena("ASDFGHJKLasdfg123458")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La contraseña no tiene el número mínimo de símbolos indicados")

    def test_comprobar_sha256(self):
        c1 = Contrasenya("Abc12_", 5, 1, 1, 1, 1)
        self.assertEqual(c1.sha256(), "898bf06d7968a29297d0615b9dc42485c40758cdd823f12a018a462b0faca481")

    def test_comprobar_sha512(self):
        c1 = Contrasenya("Abc12_", 5, 1, 1, 1, 1)
        self.assertEqual(c1.sha512(), "ba4439f846b6e688d067c2864fd1633fa10c3a834c4fc3d9355ad5f6bff78a70c5ca249a71c47237da0a5da5c440473676a940405a272a48e2d9112e617ae849")

    def test_comprobar_md5(self):
        c1 = Contrasenya("Abc12_", 5, 1, 1, 1, 1)
        self.assertEqual(c1.md5(), "57433f9fe301bc58dd24a1ca6c9fd70c")



if __name__ == '__main__':
    unittest.main()