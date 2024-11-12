from django.shortcuts import  render

def homepage(request):
    dados = {
        "titulo_pagina": "Bem Vindo ao curso do ICS",
        "subtitulo_pagina": "Curso de programção com Python e Django",
        "visitas": 123,
        "lista_visitas": [
            "Gustavo",
            "Kaique",
            "Luiz",
            "Sara L",
            "Sara M",
            "Maria Clara",
            "Ana ju",
            "Ana",
            "Gregory"
        ]
    }
    return render(request, "index.html", dados)

def clientes(request):
    return render(request, "clientes.html")

def produtos(request):
    return render(request, "produtos.html")