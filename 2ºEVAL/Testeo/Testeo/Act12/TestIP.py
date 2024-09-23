import unittest

from main import ip_ok


class test_IPs(unittest.TestCase):

    def test_IPCorrecta(self):
        resultado = ip_ok("1.2.3.4")
        self.assertEqual(resultado, True)
        resultado = ip_ok("192.168.1.2")
        self.assertEqual(resultado, True)
        resultado = ip_ok("10.1.35.10")
        self.assertEqual(resultado, True)


    def test_IPIncorrecta(self):
        resultado = ip_ok("1.2.3.259")
        self.assertEqual(resultado, False)
        resultado = ip_ok("500.1.1.1")
        self.assertEqual(resultado, False)
        resultado = ip_ok("1.1")
        self.assertEqual(resultado, False)
        resultado = ip_ok("1.-1.1.1")
        self.assertEqual(resultado, False)



if __name__ == '__main__':
    unittest.main()
