from django.shortcuts import render
from produtos.models import Produto
from contato.models import Contato

def home(request):
    return render(request, "home.html")

def Produtos(request):
    todos_os_produtos = Produto.objects.all()
    produtos_loja = {
        "lista_produtos": todos_os_produtos
    }
   
    return render(request, "Produtos.html", produtos_loja)

def Sobre_a_loja(request):
    return render(request, "Sobre_a_loja.html")

def definir_Contato(request):
    if request.method == "POST":
        _nome = request.POST.get("nome")
        _email = request.POST.get("email")
        _mensagem = request.POST.get("mensagem")
        contato = Contato(nome=_nome, email=_email, mensagem=_mensagem)
        contato.save()
        dados = {
            "mensagem": "Seu contato foi enviado com sucesso!"
        }
        return render(request, "Contato.html", dados)

    else:
        return render(request, "Contato.html")
