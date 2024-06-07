temperaturas = [23, 20, 19, 22, 30, 25,]

maior_temperatura = temperaturas[0]
menor_temperatura = temperaturas[0]
contador = 0

while contador < len(temperaturas):
    temperatura = temperaturas[contador]
    if temperatura > maior_temperatura:
       maior_temperatura = temperatura
    if temperatura < menor_temperatura:
       menor_temperatura = temperatura

    contador += 1

print("A maior temperatura é " + str(maior_temperatura))
print("A menor temperatura é " + str(menor_temperatura))

    
