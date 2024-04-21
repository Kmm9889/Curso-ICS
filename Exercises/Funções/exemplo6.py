# Crie uma função que receba 2 numeros e retorne "Maior que 100" se a soma dos 2 numeros for maior que 100

def calcula_maior_100(num1, num2):
    res = num1 + num2

    if res > 100:
        return "Maior que 100"
    else:
        return "Menor ou igual a 100"
    

resposta = calcula_maior_100(90,20)
print(resposta)

resposta = calcula_maior_100(90,9)
print(resposta)

resposta = calcula_maior_100(90,10)
print(resposta)

resposta = calcula_maior_100(90,11)
print(resposta)