from django.shortcuts import render

contato_sobre_a_empresa = {
    "contato": [ "Empresa X,",
    "Endereço Rua Exemplo, 123, Bairro Centro, Cidade, Estado, CEP 00000-000,",
    "Telefone (11) 1234-5678,",
    "E-mail contato@empresaX.com.br,",
    "Site: www.empresaX.com.br,",
    "Redes Sociais: @empresaX Instagram, Facebook, LinkedIn"]
    }

def contato(request):
    return render(request, "contato.html", contato_sobre_a_empresa)

def sobre(request):
    return render(request, "sobre.html",)