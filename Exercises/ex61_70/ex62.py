alturas = [165, 170, 180, 175, 160,]

def somar_todos_os_numeros(Lista):
    soma = 0
    for numero in Lista:
        soma += numero
    return soma
def calcular_media(alturas):
    soma = somar_todos_os_numeros(alturas)
    media = soma / len(alturas)
    return media

media_de_tudo = calcular_media(alturas)
print(media_de_tudo)