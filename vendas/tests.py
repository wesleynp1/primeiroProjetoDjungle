from django.test import TestCase
from django.urls import reverse
from .models import Venda
from .models import Cliente
from .models import Produto

# Não esqueça que teste tem que começam com a palavra 'test'
class TesteDeVendas(TestCase):
    def teste_mostrar_vendas(self):
        clientes = self._cria_clientes_ficticios()
        produtos = self._cria_produtos_ficticios()
        Venda.objects.create(cliente=clientes[0],produto=produtos[0],quantidade=15)

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
        produtos = self._cria_produtos_ficticios()
        clientes = self._cria_clientes_ficticios()

        data = { "quantidade": 15, "cliente": "45346678910", "produto": 1 }
        resposta = self.client.post(reverse("vendas:add"),data)

        venda = Venda.objects.get(cliente=clientes[0].cpf, produto=produtos[0].id)

        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(venda.produto, produtos[0])
        self.assertEqual(venda.cliente, clientes[0])

    def teste_form_delete_venda(self):
        produtos = self._cria_produtos_ficticios()
        clientes = self._cria_clientes_ficticios()

        venda = Venda.objects.create(cliente=clientes[0],produto=produtos[0],quantidade=10)

        resposta = self.client.get(reverse("vendas:delete_form",kwargs={"id":1}))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "form")
        self.assertContains(resposta, clientes[0].nome)
        self.assertContains(resposta, produtos[0].nome)
        self.assertContains(resposta, "csrf")

    def teste_delete_venda(self):
        produtos = self._cria_produtos_ficticios()
        clientes = self._cria_clientes_ficticios()
        vendas = self._cria_vendas_ficticios()

        resposta = self.client.post(reverse("vendas:delete",kwargs={"id":1}),{"id":vendas[0].id})
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(Venda.objects.all().filter(id=vendas[0].id).count(), 0)

    def teste_form_edit_venda(self):
        produtos = self._cria_produtos_ficticios()
        clientes = self._cria_clientes_ficticios()
        vendas = Venda.objects.create(produto=produtos[0],cliente=clientes[0],quantidade=10)
        resposta = self.client.get(reverse("vendas:edit_form",kwargs={"id":1}))

        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "form")
        self.assertContains(resposta, produtos[0].nome)
        self.assertContains(resposta, clientes[0].nome)
        self.assertContains(resposta, "csrf")

    def teste_edit_venda(self):
        produtos = self._cria_produtos_ficticios()
        clientes = self._cria_clientes_ficticios()
        venda = Venda.objects.create(produto=produtos[0],cliente=clientes[0],quantidade=10)

        venda_pre_alteracao = Venda.objects.get(id=venda.id)
        self.assertEqual(venda_pre_alteracao.produto, produtos[0])
        self.assertEqual(venda_pre_alteracao.cliente, clientes[0])
        self.assertEqual(venda_pre_alteracao.quantidade, 10)

        novos_dados = {"produto":produtos[1].id, "cliente":clientes[2].cpf, "quantidade":5}
        resposta = self.client.post(reverse("vendas:edit",kwargs={"id":1}),novos_dados)
        self.assertEqual(resposta.status_code, 302)

        venda_alterada = Venda.objects.get(id=venda.id)
        self.assertEqual(venda_alterada.produto, produtos[1])
        self.assertEqual(venda_alterada.cliente, clientes[2])
        self.assertEqual(venda_alterada.quantidade, 5)

    def _cria_clientes_ficticios(self):
        return [
            Cliente.objects.create(nome='ClienteA', cpf='45346678910', telefone="21912345678"),
            Cliente.objects.create(nome='ClienteB', cpf='34561278912', telefone="21912345677"),
            Cliente.objects.create(nome='ClienteC', cpf='23415678913', telefone="21912345675"),
            Cliente.objects.create(nome='ClienteD', cpf='45612378915', telefone="21912345674")
        ]

    def _cria_produtos_ficticios(self):
        return [
            Produto.objects.create(nome='ProdutoA', preco=2.99),
            Produto.objects.create(nome='ProdutoB', preco=259.99),
            Produto.objects.create(nome='ProdutoC', preco=1252.99),
            Produto.objects.create(nome='ProdutoD', preco=9872.99)
        ]

    def _cria_vendas_ficticios(self):
        produtos = Produto.objects.all()
        clientes = Cliente.objects.all()

        return [
            Venda.objects.create(cliente=clientes[2],produto=produtos[2],quantidade=5),
            Venda.objects.create(cliente=clientes[1],produto=produtos[0],quantidade=7),
            Venda.objects.create(cliente=clientes[0],produto=produtos[3],quantidade=1),
            Venda.objects.create(cliente=clientes[3],produto=produtos[1],quantidade=2)
        ]
