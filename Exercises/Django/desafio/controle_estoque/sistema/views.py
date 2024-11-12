from django.shortcuts import render

def controle_estoque(request):
    produtos = [
    {
        "nome": "Celular",
        "marca": "Samsung",
        "preco": 1500.00,
        "estoque": 30
    },
    {
        "nome": "Notebook",
        "marca": "Dell",
        "preco": 3500.00,
        "estoque": 15
    },
    {
        "nome": "Tablet",
        "marca": "Apple",
        "preco": 2800.00,
        "estoque": 25
    },
    {
        "nome": "Fone de Ouvido",
        "marca": "Sony",
        "preco": 300.00,
        "estoque": 50
    },
    {
        "nome": "Smartwatch",
        "marca": "Xiaomi",
        "preco": 800.00,
        "estoque":40
        }
]
    dados = {"produtos": produtos}
    return render(request, "controle_estoque.html", dados)