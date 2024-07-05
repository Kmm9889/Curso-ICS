
lista = [1, 2, 3, 4]

def produto_lista(numeros):
    produto = 1
    for numero in numeros:
        produto *= numero
    return produto

resultado = produto_lista(lista)
print(resultado)