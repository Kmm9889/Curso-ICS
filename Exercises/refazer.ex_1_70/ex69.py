def shift(lst):
    if lst:
        return lst.pop(0) #pop significa retornar ou remover
    else:
        return None

lista_elementos = [1, 2, 3, 4, 5]

while lista_elementos:
    elemento = shift(lista_elementos)
    print(elemento)