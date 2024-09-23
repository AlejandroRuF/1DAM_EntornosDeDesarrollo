import unittest
from coche import Coche


class TestCoche(unittest.TestCase):

    def test_coche_correcto(self):
        c1 = Coche("Ford","Focus","XZ")
        c1.maximos_ocupantes=4
        c1.llena_deposito()
        c1.subir_ocupante()
        c1.set_matricula("1234BCD")
        for i in range(3):
            c1.conducir()

    def test_cocheERROR(self):
        with self.assertRaises(Exception) as cm:
            c1 = Coche(1, "Focus", "XZ")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Tipo de dato incorrecto para la marca")

        with self.assertRaises(Exception) as cm:
            c1 = Coche("fORD", 1, "XZ")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Tipo de dato incorrecto para el modelo")

        with self.assertRaises(Exception) as cm:
            c1 = Coche("Ford", "Focus", 1)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Tipo de dato incorrecto para el tipo")

    def test_getset_matricula(self):
        c1 = Coche("Seat", "Ibiza", "Z500")
        nmatricula="1234BCD"
        c1.set_matricula(nmatricula)
        self.assertEqual(c1.get_matricula(), nmatricula)

    def test_matriculaOK(self):
        c1 = Coche("Kia", "Niro", "AS")
        nmatricula = "1234BCD"
        c1.set_matricula(nmatricula)
        nmatricula = "9876ZXY"
        c1.set_matricula(nmatricula)

    def test_matriculaERROR(self):
        c1 = Coche("Kia", "Niro", "AS")
        with self.assertRaises(Exception) as cm:
            nmatricula = 1234
            c1.set_matricula(nmatricula)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Tipo de dato incorrecto para la matrícula")

        with self.assertRaises(Exception) as cm:
            nmatricula = "A234567"
            c1.set_matricula(nmatricula)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Formato incorrecto en el primer digito de la matrícula")

        with self.assertRaises(Exception) as cm:
            c1 = Coche("Kia", "Niro", "AS")
            nmatricula = "AWS"
            c1.set_matricula(nmatricula)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Longitud incorrecta de matrícula")

        with self.assertRaises(Exception) as cm:
            c1 = Coche("Kia", "Niro", "AS")
            nmatricula = "AWS12345WES"
            c1.set_matricula(nmatricula)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Longitud incorrecta de matrícula")

        with self.assertRaises(Exception) as cm:
            nmatricula = "1A34567"
            c1.set_matricula(nmatricula)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Formato incorrecto en el segundo digito de la matrícula")

        with self.assertRaises(Exception) as cm:
            nmatricula = "12A4567"
            c1.set_matricula(nmatricula)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Formato incorrecto en el tercer digito de la matrícula")

        with self.assertRaises(Exception) as cm:
            nmatricula = "123A567"
            c1.set_matricula(nmatricula)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Formato incorrecto en el cuarto digito de la matrícula")

        with self.assertRaises(Exception) as cm:
            nmatricula = "1234567"
            c1.set_matricula(nmatricula)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Formato incorrecto en la primera letra de la matrícula")

        with self.assertRaises(Exception) as cm:
            nmatricula = "1234B67"
            c1.set_matricula(nmatricula)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Formato incorrecto en la segunda letra de la matrícula")

        with self.assertRaises(Exception) as cm:
            nmatricula = "1234BB7"
            c1.set_matricula(nmatricula)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Formato incorrecto en la tercera letra de la matrícula")

    def test_llena_depositoOK(self):
        c1 = Coche("Kia", "Niro", "AS")
        self.assertEqual(c1.llena_deposito(), None)

    def test_actializa_combustiblERROR(self):
        c1 = Coche("Kia", "Niro", "AS")
        with self.assertRaises(Exception) as cm:
            c1.actualiza_combustible(-1)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Depósito vacío.")

        with self.assertRaises(Exception) as cm:
            c1.actualiza_combustible(80)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Capacidad excedida.")

    def test_actializa_combustiblOK(self):
        c1 = Coche("Kia", "Niro", "AS")
        self.assertEqual(c1.actualiza_combustible(22), None)

    def test_obtener_combustibleOK(self):
        c1 = Coche("Kia", "Niro", "AS")
        c1.actualiza_combustible(22)
        self.assertEqual(c1.obtener_combustible(22),None)

    def test_obtener_combustibleERROR(self):
        c1 = Coche("Kia", "Niro", "AS")
        with self.assertRaises(Exception) as cm:
            c1.obtener_combustible(500)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "No es posible llenar tanto el depósito.")

    def test_subir_ocupanteERROR(self):
        c1 = Coche("Kia", "Niro", "AS")

        with self.assertRaises(Exception) as cm:
            c1.subir_ocupante()
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "No es posible llevar tantos ocupantes en el coche.")

    def test_subir_ocupanteOK(self):
        c1 = Coche("Kia", "Niro", "AS")
        c1.maximos_ocupantes = 1
        self.assertEqual(c1.subir_ocupante(), None)

    def test_conducirERROR(self):
        c1 = Coche("Kia", "Niro", "AS")
        with self.assertRaises(Exception) as cm:
            c1.conducir()
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "No es posible conducir sin matrícula.")

        c1.set_matricula("1234BCD")
        c1.maximos_ocupantes = 1

        with self.assertRaises(Exception) as cm:
            c1.conducir()
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Debe de haber al menos un ocupante para conducir el coche.")

    def test_bajar_ocupanteERROR(self):
        c1 = Coche("Kia", "Niro", "AS")
        with self.assertRaises(Exception) as cm:
            c1.bajar_ocupante()
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "No es posible.")

    def test_bajar_ocupanteOK(self):
        c1 = Coche("Kia", "Niro", "AS")
        c1.maximos_ocupantes = 1
        c1.subir_ocupante()
        self.assertEqual(c1.bajar_ocupante(), None)

    def test_pinchazoERROR(self):
        c1 = Coche("Kia", "Niro", "AS")
        c1.numero_ruedas_correctas = 0
        with self.assertRaises(Exception) as cm:
            c1.pinchazo()
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "No es posible pinchar tantas ruedas.")

    def test_pinchazoOK(self):
        c1 = Coche("Kia", "Niro", "AS")
        c1.numero_ruedas_correctas = 4
        self.assertEqual(c1.pinchazo(),None)

    def test_reparar_pinchazoERROR(self):
        c1 = Coche("Kia", "Niro", "AS")
        c1.numero_ruedas_correctas = 4
        with self.assertRaises(Exception) as cm:
            c1.reparar_pinchazo()
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "No es posible reparar tantas ruedas.")

    def test_reparar_pinchazoOK(self):
        c1 = Coche("Kia", "Niro", "AS")
        c1.numero_ruedas_correctas = 3
        self.assertEqual(c1.pinchazo(), None)


if __name__ == '__main__':
    unittest.main()
