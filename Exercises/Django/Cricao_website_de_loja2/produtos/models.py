from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    estoque = models.IntegerField()
    codigo = models.CharField(max_length=30)
    disponibilidade = models.BooleanField()
    data_cadastro = models.DateField()
    foto_produto = models.ImageField(upload_to='produtos', blank=True, null=True)

    def _str_(self):
        return "nome do produto: " + self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    slug = models.SlugField(max_length=200)

    def _str_(self):
        return "Nome da categoria: " + self.nome
    
class Grupo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    codigo = models.CharField(max_length=100)

    def _str_(self):
        return "Nome do grupo de produtos: " + self.nome
