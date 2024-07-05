matriz_numeros = [[3, 5, 1, 7], [10, 2, 8], [6, 9, 4]]

ultima_sublista = matriz_numeros[-1]
maior_numero = ultima_sublista[0]

for numero in ultima_sublista:
    if numero > maior_numero:
        maior_numero = numero

print("O maior número na Ultima sublista é:",(maior_numero))