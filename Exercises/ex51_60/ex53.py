lista_de_entrada = [5, 3, 9, 1, 10,]

def somar_todos_os_numeros(Lista):
    soma = 0
    for numero in Lista:
        soma += numero
    return soma
soma_de_tudo = somar_todos_os_numeros(lista_de_entrada)
print(soma_de_tudo)