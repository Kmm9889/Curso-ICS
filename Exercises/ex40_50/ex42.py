"2 - Palavras com Mais de 4 Caracteres:"

"Lista de entrada: [maçã, banana, kiwi, abacate, uva]"
"Função: Retorna uma lista apenas com as palavras que têm mais de 4 caracteres."


lista_de_entrada =  ["maçã", "banana", "Kiwi", "Abacate", "uva", ]

for palavra in range(len(lista_de_entrada)):
    nomes_de_frutas = lista_de_entrada[palavra]
    if (len(nomes_de_frutas)) > 4:
       print(nomes_de_frutas)

