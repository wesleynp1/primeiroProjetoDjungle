from django.test import TestCase
from loja.models import Produto
from django.urls import reverse
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

    def teste_no_view(self):
        p1 = Produto.objects.create(nome="Produto Legal", preco=1.99)
        Produto.objects.create(nome="Produto Legal 2", preco=5.99)

        resposta = self.client.get(reverse('loja:index'))
        self.assertContains(resposta,"Produto Legal")
        self.assertContains(resposta, "R$ 1,99")#Formatação realizada no backend
        self.assertQuerySetEqual(resposta.context['produtos'], Produto.objects.all(), ordered=False)#não esqueça do ordered=False

        resposta = self.client.get(reverse('loja:edit_form', args=[p1.id]))
        self.assertContains(resposta,"Produto Legal")
        self.assertContains(resposta, "1.99")#Javacript não é executado, a resposta é só o HTML

    def teste_adicionar_novo_produto(self):
        self.client.post(reverse('loja:add'), data={"nome": "Produto Legal 3", "preco": 3.99})
        self.assertContains(self.client.get(reverse('loja:index')), "Produto Legal 3",1,200)

    def teste_editar_produto(self):
        self.client.post(reverse('loja:add'), data={"nome": "Produto Legal 3", "preco": 3.99})
        self.assertContains(self.client.get(reverse('loja:index')), "Produto Legal 3",1,200)