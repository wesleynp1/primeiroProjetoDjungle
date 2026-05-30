from django.test import TestCase
from django.urls import reverse

from clientes.models import Cliente


# Create your tests here.
class ClienteTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(cpf="12345678910",nome="ana",telefone="21958694712")
        self.cliente = Cliente.objects.create(cpf="12343218910", nome="bob", telefone="21989798456")

    def teste_add_cliente_get(self):
        resposta = self.client.get(reverse("clientes:add_form"))
        self.assertEqual(resposta.status_code, 200)

    def teste_add_cliente_post(self):
        cliente_dados = {
            "cpf": "12345678911",
            "nome": "maria",
            "telefone": "21958694712",
        }
        resposta2 = self.client.post(
            reverse("clientes:add"),
            cliente_dados
        )
        self.assertEqual(resposta2.status_code, 302)

        cliente_adicionado = Cliente.objects.get(cpf=cliente_dados["cpf"])

        self.assertEqual(cliente_adicionado.nome,cliente_dados["nome"])
        self.assertEqual(cliente_adicionado.cpf, cliente_dados["cpf"])
        self.assertEqual(cliente_adicionado.telefone, cliente_dados["telefone"])

    def teste_delete_cliente_get(self):
        resposta = self.client.get(reverse("clientes:delete_form",args=["12343218910"]))
        self.assertEqual(resposta.status_code, 200)

    def teste_delete_cliente_post(self):
        resposta = self.client.post(reverse("clientes:delete",args=["12343218910"]))
        self.assertEqual(resposta.status_code,302)

    def teste_edit_cliente_get(self):
        resposta = self.client.get(reverse("clientes:edit_form",args=["12343218910"]))
        self.assertEqual(resposta.status_code, 200)

    def teste_edit_cliente_post(self):
        cliente_dados = {"nome":"carla", "telefone":"21968694712"}
        resposta = self.client.post(reverse("clientes:edit",args=["12343218910"]), cliente_dados)
        self.assertEqual(resposta.status_code,302)

        cliente_editado = Cliente.objects.get(cpf="12343218910")
        self.assertEqual(cliente_editado.nome,cliente_dados["nome"])
        self.assertEqual(cliente_editado.telefone, cliente_dados["telefone"])