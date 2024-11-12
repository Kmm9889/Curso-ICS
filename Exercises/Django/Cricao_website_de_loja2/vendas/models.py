from django.db import models

class Venda(models.Model):
    data = models.DateTimeField(max_length=15)
    valor_total = models.DecimalField(decimal_places=2, max_digits=8)
    forma_pagamento = models.CharField(max_length=40)
    observacao = models.TextField(max_length=500)

    def __str__(self):
        return "valor total da venda: " + self.valor_total

class Cobranca(models.Model):
    valor =  models.DecimalField(decimal_places=2, max_digits=8)
    status = models.CharField(max_length=10)
    data_vencimento = models.DateField(max_length=10)
    data_pagamento = models.DateField(max_length=10)
    metodo = models.CharField(max_length=10)

    def __str__(self):
        return "valor da cobrança: " + self.valor

class Entrega(models.Model):
    endereco_entrega = models.CharField(max_length=50)
    data_envio = models.DateField(max_length=10)
    data_entrega = models.DateField(max_length=10)
    status = models.CharField(max_length=20)
    codigo_rastreamento = models.CharField(max_length=50)

    def __str__(self):
        return "endereço da entrega: " + self.endereco_entrega
