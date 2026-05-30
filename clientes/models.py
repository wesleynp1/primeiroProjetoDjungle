from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf  = models.CharField(max_length=11, primary_key=True)
    telefone = models.CharField(max_length=13,null=True, blank=True)