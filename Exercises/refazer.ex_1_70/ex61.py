numeros_pares = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista_de_numeros_pares = []

for numero in numeros_pares:
    if numero % 2 == 0:
        lista_de_numeros_pares.append(numero)

print(lista_de_numeros_pares)