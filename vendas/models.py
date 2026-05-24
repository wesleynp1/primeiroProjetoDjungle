from django.db import models
from loja.models import Produto
from loja.models import Cliente
from wnp.formatBRL import formatBRL

# Create your models here.
class Venda(models.Model):
    produto    = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente    = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def get_total(self):
        return formatBRL.preco_formatado(self.quantidade * self.produto.preco)