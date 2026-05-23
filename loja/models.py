from django.db import models

class Produto(models.Model):
    nome  = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f'É um {self.nome}, custando {self.preco.__str__().replace(".", ",")} reais.'

    def preco_formatado(self):
        preco_em_str = f'{self.preco:.2f}'

        if(self.preco > 999.99): #irá precisar do ponto separador dos milhares
            # transforma em str e separa os reais dos centavos
            [reais, centavos] = preco_em_str.split(".")

            #adiciona o ponto separador dos milhares
            reais = list(reais)
            for i in range(len(reais)-3,0,-3):
                reais.insert(i,".")

            return  f'R$ {"".join(reais)},{centavos}'
        else:
            return f'R$ {preco_em_str.replace(".", ",")}'

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf  = models.CharField(max_length=11, primary_key=True)
    telefone = models.CharField(max_length=13,null=True, blank=True)

class Venda(models.Model):
    produto    = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente    = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quantidade = models.IntegerField()