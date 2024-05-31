
"1 - Números Pares:Lista de entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9]"
"Função: Retorna uma lista apenas com os números pares."


lista_de_entrada =  [1,2,3,4,5,6,7,8,9]

for numero in range(len(lista_de_entrada)):
    numero_a_ser_testado = lista_de_entrada[numero]
    if numero_a_ser_testado % 2 == 0:
        print(numero_a_ser_testado)
