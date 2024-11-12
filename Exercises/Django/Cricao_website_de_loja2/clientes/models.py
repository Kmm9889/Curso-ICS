from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email =  models.EmailField(max_length=60)
    telefone = models.CharField(max_length=40)
    endereco = models.CharField(max_length=150)
    data_de_nascimento = models.DateField(max_length=10)
    ativo = models.BooleanField()

    def __str__(self):
        return "nome: " + self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    descriacao = models.TextField(max_length=500)

    def __str__(self):
        return "categoria: " + self.nome
