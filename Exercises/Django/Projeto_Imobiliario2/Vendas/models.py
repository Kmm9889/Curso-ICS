from django.db import models
from django.db import models

class Venda(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    estoque = models.IntegerField()
    endereço = models.CharField(max_length=30)
    disponibilidade = models.BooleanField()
    data_da_e_hora_da_compra = models.DateTimeField()
    foto_da_casa = models.ImageField(upload_to='Vendas', blank=True, null=True)

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    nome_da_casa_a_ser_reservada = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    estoque = models.IntegerField()
    endereço = models.CharField(max_length=30)
    disponibilidade = models.BooleanField()
    data_da_reserva = models.DateTimeField()
    foto_da_casa = models.ImageField(upload_to='Reserva', blank=True, null=True)

    def __str__(self):
        return self.nome_da_casa_a_ser_reservada
