from django.shortcuts import render

Todos_os_produtos = {
    "Todos_os_produtos":[
        "Sofá",
        "Cadeira",
        "Estante",
        "Mesa de centro",
        "telefone",
        "Caixa de som",
        "Celulares",
        "Notebooks",
        "Projetores",
        "impressora"
    ]
}

dados_sobre_moveis = {
        "produtos_moveis":[
        "Sofá",
        "Cadeira",
        "Estante",
        "Mesa de centro",]
       }

dados = {
        "produtos_eletronicos":[
        "telefone",
        "Caixa de som",
        "Celulares",
        "Notebooks",
        "Projetores",
        "impressora"]
       }

def produtos_eletronicos(request):
    return render(request, "produtos_eletronicos.html", dados)

def produtos_moveis(request):
    return render(request, "produtos_moveis.html", dados_sobre_moveis)

def todos_os_produtos(request):
    return render(request, "todos_os_produtos.html", Todos_os_produtos)
