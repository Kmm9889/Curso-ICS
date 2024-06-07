duplicar = [1,2]

def duplicar_elementos(dobrar):
    dobrar_elementos = []
    for elemento in dobrar:
        dobrar_elementos.append(elemento)
        dobrar_elementos.append(elemento)
    return dobrar_elementos

lista_duplicada = duplicar_elementos(duplicar)
print(lista_duplicada)