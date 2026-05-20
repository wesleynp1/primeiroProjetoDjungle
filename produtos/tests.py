from django.test import TestCase
from produtos.models import Produto
# Create your tests here.

class TesteDeProduto(TestCase):
    def teste_formatacao_reais(self):
        p = Produto()

        p.preco = 9871234567890.99
        self.assertEqual(p.preco_formatado(), "R$ 9.871.234.567.890,99")

        p.preco = 1_234_567_890.99
        self.assertEqual(p.preco_formatado(), "R$ 1.234.567.890,99")

        p.preco = 4_567_890.99
        self.assertEqual(p.preco_formatado(), "R$ 4.567.890,99")

        p.preco = 90.99
        self.assertEqual(p.preco_formatado(), "R$ 90,99")

        p.preco = 90.0
        self.assertEqual(p.preco_formatado(), "R$ 90,00")