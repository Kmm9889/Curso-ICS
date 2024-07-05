lista_menor = (1,2,3,4,2)

def acha_menor(lista):
    menor_numero = lista[0]

    for numero in lista:
        if numero < menor_numero:
           menor_numero = numero

    return menor_numero

res = acha_menor(lista_menor)
print(res)
        
