import unittest

from fizzbuzz import process


class test_fizzbuzz(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(Exception) as cm:
            process("fizzbuzz")
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0], "No es un número entero")

    def test_numeros_negativos(self):
        with self.assertRaises(Exception) as cm:
            process(-10)
        self.assertEqual(len(cm.exception.args), 1)
        self.assertEqual(cm.exception.args[0],"No se admiten números negativos")

    def test_divisbleen_3_y_5(self):
        self.assertEqual(process(15), "FizzBuzz")
        self.assertEqual(process(30), "FizzBuzz")
        self.assertEqual(process(45), "FizzBuzz")

    def test_divisible_3(self):
        self.assertEqual(process(3), "Fizz")
        self.assertEqual(process(6), "Fizz")
        self.assertEqual(process(27), "Fizz")

    def test_divisible_5(self):
        self.assertEqual(process(5), "Buzz")
        self.assertEqual(process(10), "Buzz")
        self.assertEqual(process(20), "Buzz")

    def test_nodivisible_3_ni_5(self):
        self.assertEqual(process(7), 7)
        self.assertEqual(process(41), 41)
        self.assertEqual(process(8), 8)


if __name__ == '__main__':
    unittest.main()
