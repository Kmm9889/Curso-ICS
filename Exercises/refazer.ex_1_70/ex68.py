triplicar = [3,4]

def triplicar_elementos(triplicar):
    triplicar_elementos = []
    for elemento in triplicar:
        triplicar_elementos.append(elemento)
        triplicar_elementos.append(elemento)
        triplicar_elementos.append(elemento)
    return triplicar_elementos

lista_triplicada = triplicar_elementos(triplicar)
print(lista_triplicada)