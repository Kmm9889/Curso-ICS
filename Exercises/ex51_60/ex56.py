lista_palavras = ["Ola, eu moro em Buritizeiro"]

for numero in range(len(lista_palavras)):
    lista_palavras[numero] = lista_palavras[numero].replace("Buritizeiro", "São Romão")
    
print(lista_palavras)

#replace é uma função de string em Python que permite substituir todas as ocorrências de uma substring (parte da string) por outra substring