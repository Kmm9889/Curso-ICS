alturas = [165, 170, 180, 175, 160]
soma = 0

def somar_alturas(lista):
    soma = 0
    for numero in alturas:
       soma += numero
    return soma
def calcular_media(alturas):
    soma = somar_alturas(alturas)
    media = soma / len(alturas)
    return media

media_de_tudo = calcular_media(alturas)
print(media_de_tudo)

