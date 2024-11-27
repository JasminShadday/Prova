import unittest
from main import exibir_mensagem

class TestExibirMensagem(unittest.TestCase):

    def test_exibir_mensagem(self):

        resultado = exibir_mensagem()

        self.assertIsInstance(resultado, dict)
 
        self.assertIn('sms', resultado)
        self.assertEqual(resultado['sms'], 'Hello, DevOps!')

        self.assertIn('status', resultado)
        self.assertEqual(resultado['status'], 200)


if __name__ == '__main__':
    unittest.main()
