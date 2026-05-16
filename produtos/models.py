from django.db import models

class Produto(models.Model):
    nome  = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f'É um {self.nome}, custando {self.preco.__str__().replace(".", ",")} reais.'

class cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf  = models.CharField(max_length=11, primary_key=True)

class venda(models.Model):
    produto    = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente    = models.ForeignKey(cliente, on_delete=models.CASCADE)
    quantidade = models.IntegerField()