from django.shortcuts import render
from Contato.models import Contato

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