dicionario = {
    "Brasil": "Brasília",
    "Belgica": "Bruxelas",
    "Argentina": "Buenos Aires",
    "Alemanha": "Berlim",
    "Egito": "Cairo"
}

def contar_ocorrencias(palavras):
    contar = {}
    for palavra in palavras:
        if palavra in contar:
            contar[palavra] += 1
        else:
            contar[palavra] = 1
    
    return contar

resultado = contar_ocorrencias(dicionario)
print(resultado)