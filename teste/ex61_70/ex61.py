numeros_pares = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def seleciona_numeros_pares(numeros_pares):
    contador = 0
    Lista_auxiliar = []

    while contador < len(numeros_pares):
       numero = numeros_pares[contador]
       if numero % 2 == 0:
        Lista_auxiliar.append(numero)
       contador += 1

    return Lista_auxiliar

lista_de_numeros_pares = seleciona_numeros_pares(numeros_pares)
print(lista_de_numeros_pares)
