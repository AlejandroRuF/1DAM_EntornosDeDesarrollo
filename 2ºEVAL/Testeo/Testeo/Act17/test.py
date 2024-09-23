import unittest

from cuenta import Persona
from cuenta import Compte

class test_cuenta(unittest.TestCase):
    def test_crear_personaOK(self):
        persona1 = Persona("Paco", 28, "64393419C")

    def test_crear_personaERROR(self):
        with self.assertRaises(Exception) as cm:
            persona1 = Persona("12", 28, "64393419C")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El nombre solo puede admitir carácteres alfabéticos")

        with self.assertRaises(Exception) as cm:
            persona1 = Persona("Paco", "28", "64393419C")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "No es una edad válida")

        with self.assertRaises(Exception) as cm:
            persona1 = Persona("Paco", -1, "64393419C")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "No es una edad válida")


    def test_es_major_edad(self):
        persona1 = Persona("Paco", 28, "64393419C")
        self.assertEqual(persona1.es_major_edat(), None)
        persona1 = Persona("Paco", 2, "64393419C")
        self.assertEqual(persona1.es_major_edat(), None)

    def test_letra_dni(self):
        persona1 = Persona("Paco", 28, "64393419C")
        self.assertEqual(persona1.lletra_dni(), "C")

    def test_comprobar_dniError(self):
        persona1 = Persona("Paco", 28, "64393419C")
        with self.assertRaises(Exception) as cm:
            persona1.dni = "64393419A"
            persona1.comprobar_dni()
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Formato del DNI incorrecto")

        with self.assertRaises(Exception) as cm:
            persona1.dni = "4393419A"
            persona1.comprobar_dni()
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La longitud del DNI es incorrecta")


class test_compte(unittest.TestCase):
    def test_creacion_compteOK(self):
        p1 = Persona("Paco", 28, "64393419C")
        c1 = Compte(p1,500)

    def test_creacion_compteERROR(self):
        p1 = Persona("Paco", 28, "64393419C")

        with self.assertRaises(Exception) as cm:
            c1 = Compte("paco",500)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El parámetro no es el tipo Persona")

        with self.assertRaises(Exception) as cm:
            c1 = Compte(p1,"500")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Saldo inicial incorrecto")

    def test_resumen(self):
        p1 = Persona("Paco", 28, "64393419C")
        c1 = Compte(p1, 500)
        c1.resumen()

    def test_agregar_saldoOK(self):
        p1 = Persona("Paco", 28, "64393419C")
        c1 = Compte(p1, 500)
        self.assertEqual(c1.agregar_saldo(100), None)
        self.assertEqual(c1.agregar_saldo(1), None)
        self.assertEqual(c1.agregar_saldo(6000), None)

    def test_agregar_saldoERROR(self):
        p1 = Persona("Paco", 28, "64393419C")
        c1 = Compte(p1, 500)

        with self.assertRaises(Exception) as cm:
            c1.agregar_saldo("500")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Cantidad a agregar incorrecta")

        with self.assertRaises(Exception) as cm:
            c1.agregar_saldo(-500)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El ingreso no puede ser negativo ni cero.")

    def test_retirar_saldoOK(self):
        p1 = Persona("Paco", 28, "64393419C")
        c1 = Compte(p1, 500)
        self.assertEqual(c1.retirar_saldo(100), None)
        self.assertEqual(c1.retirar_saldo(10), None)
        self.assertEqual(c1.retirar_saldo(21), None)

    def test_retirar_saldoERROR(self):
        p1 = Persona("Paco", 28, "64393419C")
        c1 = Compte(p1, 500)

        with self.assertRaises(Exception) as cm:
            c1.retirar_saldo("10")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Cantidad a retirar incorrecta")

        with self.assertRaises(Exception) as cm:
            c1.retirar_saldo(-10)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Debe de retirar una cantidad positiva.")

        with self.assertRaises(Exception) as cm:
            c1.retirar_saldo(1000000)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Operación imposible: No dispone de suficiente saldo.")

    def test_historico(self):
        p1 = Persona("Paco", 28, "64393419C")
        c1 = Compte(p1, 500)
        c1.historic()
        c1.agregar_saldo(10)
        c1.historic()
        c1.retirar_saldo(50)
        c1.historic()


if __name__ == "__main__":
    unittest.main()

