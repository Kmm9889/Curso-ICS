"Lista de entrada: [5, 3, 9, 1, 10]"
"Função: Encontra e retorna o maior número da lista."


lista_de_entrada = [5, 3, 9, 1, 10,]

def maior_numero(lista):
    maior_numero_da_lista = lista[0]
    for numero in lista[1:]:
      if numero > maior_numero_da_lista:
         maior = numero
    return maior

resultado = maior_numero(lista_de_entrada)
print(resultado)