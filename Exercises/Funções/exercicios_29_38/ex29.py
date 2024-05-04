num1 = input("Digite o primeiro numero:")
num2 = input("Digite o segundo numero:")
operação = input("Digite qual operação você deseja: + - * /")

if operação == "+":
    soma = int(num1) + int(num2)
    print(soma)

elif operação == "-":
    subtração = int(num1) - int(num2)
    print(subtração)

elif operação == "*":
    multiplicacao = int(num1) * int(num2)
    print(multiplicacao)

else:
     operação == "/"
     divisão = int(num1) / int (num2)
     print(divisão)