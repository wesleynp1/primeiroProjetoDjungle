from django.test import TestCase
from django.urls import reverse

import vendas
from .models import Venda
from clientes.models import Cliente
from loja.models import Produto

# Não esqueça que teste tem que começam com a palavra 'test'
class TesteDeVendas(TestCase):
    def setUp(self):
        clientes = [
            Cliente.objects.create(nome='ClienteA', cpf='45346678910', telefone="21912345678"),
            Cliente.objects.create(nome='ClienteB', cpf='34561278912', telefone="21912345677"),
            Cliente.objects.create(nome='ClienteC', cpf='23415678913', telefone="21912345675"),
            Cliente.objects.create(nome='ClienteD', cpf='45612378915', telefone="21912345674")
        ]

        produtos = [
        Produto.objects.create(nome='ProdutoA', preco=2.99),
        Produto.objects.create(nome='ProdutoB', preco=259.99),
        Produto.objects.create(nome='ProdutoC', preco=1252.99),
        Produto.objects.create(nome='ProdutoD', preco=9872.99)
        ]

        Venda.objects.create(cliente=clientes[2], produto=produtos[2], quantidade=5),
        Venda.objects.create(cliente=clientes[1], produto=produtos[0], quantidade=7),
        Venda.objects.create(cliente=clientes[0], produto=produtos[3], quantidade=1),
        Venda.objects.create(cliente=clientes[3], produto=produtos[1], quantidade=2)

    def teste_mostrar_vendas(self):
        cliente = Cliente.objects.get(nome='ClienteA')
        produto = Produto.objects.get(nome='ProdutoA')
        Venda.objects.create(cliente=cliente,produto=produto,quantidade=15)

        resposta = self.client.get(reverse("vendas:index"))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "ClienteA")
        self.assertContains(resposta, "ProdutoA")

    def teste_form_add_venda(self):
        resposta = self.client.get("/vendas/form/add")
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "form")
        self.assertContains(resposta, "csrf")

    def teste_add_venda(self):
        cliente = Cliente.objects.get(nome='ClienteA')
        produto = Produto.objects.get(nome='ProdutoA')

        data = { "quantidade": 15, "cliente": "45346678910", "produto": 1 }
        resposta = self.client.post(reverse("vendas:add"),data)

        venda = Venda.objects.get(cliente=cliente.cpf, produto=produto.id)

        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(venda.produto, produto)
        self.assertEqual(venda.cliente, cliente)

    def teste_form_delete_venda(self):
        cliente = Cliente.objects.get(nome='ClienteA')
        produto = Produto.objects.get(nome='ProdutoA')

        venda = Venda.objects.create(cliente=cliente,produto=produto,quantidade=10)

        resposta = self.client.get(reverse("vendas:delete_form",kwargs={"id":venda.id}))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "form")
        self.assertContains(resposta, cliente.nome)
        self.assertContains(resposta, produto.nome)
        self.assertContains(resposta, "csrf")

    def teste_delete_venda(self):
        cliente = Cliente.objects.get(nome='ClienteA')
        produto = Produto.objects.get(nome='ProdutoA')
        venda = Venda.objects.create(cliente=cliente,produto=produto,quantidade=10)

        resposta = self.client.post(reverse("vendas:delete",kwargs={"id":venda.id}),{"id":venda.id})
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(Venda.objects.all().filter(id=venda.id).count(), 0)

    def teste_form_edit_venda(self):
        cliente = Cliente.objects.get(nome='ClienteB')
        produto = Produto.objects.get(nome='ProdutoC')

        venda = Venda.objects.create(produto=produto,cliente=cliente,quantidade=10)
        resposta = self.client.get(reverse("vendas:edit_form",kwargs={"id":venda.id}))

        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "form")
        self.assertContains(resposta, produto.nome)
        self.assertContains(resposta, cliente.nome)
        self.assertContains(resposta, "csrf")

    def teste_edit_venda(self):
        cliente = Cliente.objects.get(nome='ClienteB')
        produto = Produto.objects.get(nome='ProdutoC')
        venda = Venda.objects.create(produto=produto,cliente=cliente,quantidade=10)

        venda_pre_alteracao = Venda.objects.get(id=venda.id)
        self.assertEqual(venda_pre_alteracao.produto, produto)
        self.assertEqual(venda_pre_alteracao.cliente, cliente)
        self.assertEqual(venda_pre_alteracao.quantidade, 10)

        novos_dados = {"produto":produto.id, "cliente":cliente.cpf, "quantidade":5}
        resposta = self.client.post(reverse("vendas:edit",kwargs={"id":venda.id}),novos_dados)
        self.assertEqual(resposta.status_code, 302)

        venda_alterada = Venda.objects.get(id=venda.id)
        self.assertEqual(venda_alterada.produto, produto)
        self.assertEqual(venda_alterada.cliente, cliente)
        self.assertEqual(venda_alterada.quantidade, 5)