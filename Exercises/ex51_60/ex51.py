numeros_impares = [1,2,3,4,5,6,7,8,8,9,10,11,12,13,14,15]

def seleciona_numeros_impares(numeros_impares):
    contador = len(numeros_impares) -1
    Lista_auxiliar = []

    while contador >=0:
       numero = numeros_impares[contador]
       if numero % 2 == 1:
        Lista_auxiliar.append(numero)
       contador = contador -1

    return Lista_auxiliar

Lista_de_numeros_impares = seleciona_numeros_impares(numeros_impares)
print(Lista_de_numeros_impares)
