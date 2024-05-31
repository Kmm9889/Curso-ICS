Lista_de_entrada = ["maçã", "banana", "cereja"]

def verificar_elemento(lista, verificar):
    return verificar in lista

elemento = "banana"
resultado = verificar_elemento(Lista_de_entrada, elemento)
print(resultado)