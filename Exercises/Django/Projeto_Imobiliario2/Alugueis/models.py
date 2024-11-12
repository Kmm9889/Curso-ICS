from django.db import models

class ImovelAluguel(models.Model):
    nome_do_Imovel = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    preco_por_mes= models.DecimalField(decimal_places=2, max_digits=10)
    disponibilidade = models.BooleanField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    foto_da_casa = models.ImageField(upload_to='ImovelAluguel', blank=True, null=True)
    

    def __str__(self):
        return f"a disponibilidade desse imovel e de {self.inicio} a {self.fim}"

class Contrato(models.Model):
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[
        ('ativo', 'Ativo'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ])
    preco_a_pagar= models.DecimalField(decimal_places=2, max_digits=10)
    foto_do_contrato = models.ImageField(upload_to='Contrato', blank=True, null=True)

    def __str__(self):
        return f"esse contrato vai de {self.inicio} a {self.fim}"
    


class Contato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome