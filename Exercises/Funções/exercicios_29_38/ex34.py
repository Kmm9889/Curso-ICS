import random

def jogo_de_adivinhação():
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    print("Jogo de adivinhação")

    while True:
        palpite = int(input("Digite um número entre 1 e 10: "))
        tentativas += 1  

        if palpite == numero_secreto:
            print(f"Você acertou o número {numero_secreto} em {tentativas} Tentativas!")
            break
        elif palpite < numero_secreto:
            print("Maior")
        else:
            print("Menor")

jogo_de_adivinhação()
