import unittest

from juego import Juego


class test_juego(unittest.TestCase):

    def test_set_jugador(self):
        juego1 = Juego("Pepe",
                          "Paco",
                          6,
                          8,
                          12,
                          10,
                          "S")
        self.assertEqual(juego1.set_jugador1("Antonio"), None)
        self.assertEqual(juego1.set_jugador2("Benancio"), None)

    def test_mostrar(self):
        juego1 = Juego("Pepe",
                          "Paco",
                          6,
                          8,
                          12,
                          10,
                          "s")
        juego1.lanzamiento()
        self.assertEqual(juego1.mostrar(), None)

    def test_lanzamiento(self):
        juego1 = Juego("Pepe",
                          "Paco",
                          6,
                          8,
                          12,
                          10,
                          "S")
        gana1 = False
        gana2 = False
        empate = False
        while True:
            self.assertEqual(juego1.lanzamiento(), None)
            if juego1.resultados1 > juego1.resultados2:
                gana1 = True
                juego1.mostrar()
            elif juego1.resultados1 < juego1.resultados2:
                gana2 = True
                juego1.mostrar()
            else:
                empate = True
                juego1.mostrar()
            if gana1 and gana2 and empate:
                break



    def test_set_lanzamiento(self):
        juego1 = Juego("Pepe",
                       "Paco",
                       6,
                       8,
                       12,
                       10,
                       "S")
        juego1.lanzamiento()
        self.assertEqual(juego1.set_lanzamientos(50), None)
        self.assertEqual(juego1.set_lanzamientos(3), None)
        self.assertEqual(juego1.set_lanzamientos(99), None)



    def test_error_setLanzamiento(self):
        juego1 = Juego("Pepe",
                          "Paco",
                          6,
                          8,
                          12,
                          10,
                          "S")
        juego1.lanzamiento()
        with self.assertRaises(Exception) as cm:
            juego1.set_lanzamientos(1)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de lanzamientos debe de estar entre 2 y 100")

        with self.assertRaises(Exception) as cm:
            juego1.set_lanzamientos(2)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de lanzamientos debe de estar entre 2 y 100")

        with self.assertRaises(Exception) as cm:
            juego1.set_lanzamientos(100)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "El número de lanzamientos debe de estar entre 2 y 100")


    def test_error_nombres(self):
        juego1 = Juego("Pepe",
                          "Paco",
                          6,
                          8,
                          12,
                          10,
                          "S")
        juego1.lanzamiento()
        with self.assertRaises(Exception) as cm:
            juego1.set_jugador1("ssdfgsdfgsdfgsdfgsdfgsdfgdf1322315682")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La longitud del nombre del jugador 1 no puede ser mayor de 20")
        with self.assertRaises(Exception) as cm:
            juego1.set_jugador2("ssdfgsdfgsdfgsdfgsdfgsdfgdf1322315682")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "La longitud del nombre del jugador 2 no puede ser mayor de 20")



    def test_getters(self):
        juego1 = Juego("Pepe",
                       "Paco",
                       6,
                       8,
                       12,
                       10,
                       "S")
        juego1.lanzamiento()
        self.assertEqual(juego1.dado1.get_caras(), 6)

    def test_seter_dados(self):
        juego1 = Juego("Pepe",
                       "Paco",
                       6,
                       8,
                       12,
                       10,
                       "S")
        juego1.lanzamiento()

        with self.assertRaises(Exception) as cm:
            juego1.dado1.set_caras(5)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "Numero de caras incorrecto")


if __name__ == '__main__':
    unittest.main()
