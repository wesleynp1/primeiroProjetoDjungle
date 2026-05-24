from django.db import models
from wnp.formatBRL import formatBRL

class Produto(models.Model):
    nome  = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f'É um {self.nome}, custando {self.preco.__str__().replace(".", ",")} reais.'

    def preco_formatado(self):
        return formatBRL.preco_formatado(self.preco)

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf  = models.CharField(max_length=11, primary_key=True)
    telefone = models.CharField(max_length=13,null=True, blank=True)

