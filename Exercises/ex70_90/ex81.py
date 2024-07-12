
dicionario = {
    "Maçã": [12],
    "Banana": [10],
    "Maracujá": [11]
}

def frutas_com_valores_maiores_do_que_10(dicionario):
    novo_dicionario = {}
    for fruta, valores in dicionario.items():
        if valores[0] > 10:
            novo_dicionario[fruta] = valores
    return novo_dicionario

resultado = frutas_com_valores_maiores_do_que_10(dicionario)
print(resultado)
