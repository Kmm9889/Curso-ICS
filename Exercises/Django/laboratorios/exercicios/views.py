from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def ex1(request):
    data = {
        'titulo': 'Exercicio 1',
        'descrição': 'Olá Mundo! '
    }

    return render(request, 'ex1.html', data)

def ex2(request):
    data = {
        'titulo': 'Exercicio 2',
        'descrição': 'Calculadora de Total'
    }

    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        total = int(valor1) + int(valor2)
        data['total'] = total
    return render(request, 'ex2.html', data)

def ex3(request):
    data = {
        'titulo': 'Exercicio 3',
        'descrição': 'Imprima seu nome e sua idade na tela'
    }

    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        frase = f'Seu nome é {nome} e sua idade é {idade}'
        data['frase'] = frase
    return render (request, 'ex3.html', data)

def ex4(request):
    data = {
        'titulo': 'Exercicio 4',
        'descrição': 'Imprimir a soma de dois numeros'
    }

    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        soma = int(valor1) + int(valor2)
        data['soma'] = soma
    return render (request, 'ex4.html', data)

def ex5(request):
    data = {
        'titulo': 'Exercicio 5',
        'descrição': 'Crie um programa que imprima a quantidade de caracteres de uma palavra'
    }

    if request.method == 'POST':
        palavra = request.POST.get("palavra") 
        if palavra:
            caracteres = len(palavra)
            data['caracteres'] = caracteres
        else:
            data['caracteres'] = 0  
    return render(request, 'ex5.html', data)

def ex6(request):
    data = {
        'titulo': 'Exercicio 6',
        'descrição': 'Crie um programa com 5 variaveis, cada uma delas com uma palavra distinta, e no final o programa deve imprimir todas elas como se fosse uma frase'
    }

    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        palavra3 = request.POST.get("palavra3")
        palavra4 = request.POST.get("palavra4")
        palavra5 = request.POST.get("palavra5")
        frase = str(palavra1) + " " + str(palavra2) + " " + str(palavra3) + " " + str(palavra4) + " " + str(palavra5)
        data['frase'] = frase
    return render (request, 'ex6.html', data)

def ex7(request):
    data = {
        'titulo': 'Exercicio 7',
        'descrição': 'Crie um programa que imprima um numero somado dele mesmo'
    }

    if request.method == 'POST':
        valor = request.POST.get("valor") 
        soma = int(valor) + int(valor)
        data['soma'] = soma
    return render (request, 'ex7.html', data)

def ex8(request):
    data = {
        'titulo': 'Exercicio 8',
        'descrição': 'Crie um programa que imprima um numero somado mais 1'
    }
    if request.method == 'POST':
        valor = request.POST.get("valor") 
        soma = int(valor) + 1
        data['soma'] = soma
    return render (request, 'ex8.html', data)

def ex9(request):
    data = {
        'titulo': 'Exercicio 9',
        'descrição': 'Crie um programa que declare uma variável nome com o seu nome e, usando print, exiba a mensagem "Olá, [nome]!".'}
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        frase = f'Olá {nome}'
        data['frase'] = frase
    return render (request, 'ex9.html', data)

def ex10(request):
    data = {
        'titulo': 'Exercicio 10',
        'descrição': ' Escreva um programa que tenha duas variáveis inteiras, some esses valores e imprima o resultado da soma.'
    }

    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        soma = int(valor1) + int(valor2)
        data['soma'] = soma
    return render (request, 'ex10.html', data)

def ex11(request):
    data = {
        'titulo': 'Exercicio 11',
        'descrição': 'Desenvolva um programa que tenha uma variável do tipo string com uma frase qualquer e, com print, mostre a quantidade de caracteres dessa frase.'
    }

    if request.method == 'POST':
        palavra = request.POST.get("palavra") 
        if palavra:
            caracteres = len(palavra)
            data['caracteres'] = caracteres
        else:
            data['caracteres'] = 0  
    return render(request, 'ex11.html', data)

def ex12(request):
    data = {
        'titulo': 'Exercicio 12',
        'descrição': 'Faça um programa que contenha duas variáveis string, parte1 e parte2, atribua valores a elas, una as duas em uma terceira variável e imprima o resultado.'
    }

    if request.method == 'POST':
        parte1 = request.POST.get("parte1") 
        parte2 = request.POST.get("parte2")
        parte3 = str(parte1) + " " + str(parte2)
        data['parte3'] = parte3
    return render (request, 'ex12.html', data)

def ex13(request):
    data = {
        'titulo': 'Exercicio 13',
        'descrição': ' Crie um programa que tenha uma variável com o ano atual e outra com o ano de nascimento de uma pessoa (use valores fictícios) e imprima a idade dessa pessoa.'
    } 

    if request.method == 'POST':
        Ano_de_nascimento = request.POST.get("ano_de_nascimento") 
        ano_atual = 2024
        data_de_nascimento = int(ano_atual) - int(Ano_de_nascimento)
        data['data_de_nascimento'] = data_de_nascimento
    return render(request, 'ex13.html', data)

def ex14(request):
    data = {
        'titulo': 'Exercicio 14',
        'descrição': 'Escreva um programa que tenha duas variáveis a e b com valores numéricos, troque os valores entre elas e, em seguida, imprima os novos valores de a e b.'
        }
    
    if request.method == 'POST':
        a = request.POST.get("a")
        b = request.POST.get("b")
        troca = a, b = b, a
        data['troca'] = troca
    return render(request, 'ex14.html', data)

def ex15(request):
    data = {
        'titulo': 'Exercicio 15 ',
        'descrição': 'Desenvolva um programa que crie uma variável frase e atribua a ela uma string qualquer. Imprima essa string três vezes seguidas.'
        }
    
    if request.method == 'POST':
        frase = request.POST.get("frase") 
        frase1 = str(frase) + ' ' + str(frase) + ' ' + str(frase)
        data['frase1'] = frase1
    return render(request, 'ex15.html', data)

def ex16(request):
    data = {
        'titulo': 'Exercicio 16',
        'descrição': ' Faça um programa que declare quatro variáveis inteiras, realize a média desses valores e imprima o resultado.'
    }

    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        valor3 = request.POST.get("valor3") 
        valor4 = request.POST.get("valor4")
        media = (int(valor1) + int(valor2) + int(valor3) + int(valor4))/4
        data['media'] = media
    return render (request, 'ex16.html', data)

def ex17(request):
    data = {
        'titulo': 'Exercicio 17',
        'descrição': ' Crie um programa que tenha uma variável com uma string representando o nome de uma cor e outra variável com um objeto (por exemplo, "carro"). Imprima uma frase que combine essas informações, como "carro azul".'
    }

    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " " + str(palavra1) + " " 
        data['frase'] = frase
    return render (request, 'ex17.html', data)

def ex18(request):
    data = {
        'titulo': 'Exercicio 18',
        'descrição': 'Escreva um programa que declare duas variáveis com nomes de cidades e use print para exibir uma frase que diga que uma está a leste da outra, por exemplo, "Paris está a leste de Londres".'
    }

    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " está a leste de " + str(palavra1)
        data['frase'] = frase
    return render(request, 'ex18.html', data)

def ex19(request):
    data = {
        'titulo': 'Exercicio 19 Função Simples de Saudação',
        'descrição': 'Escreva uma função chamada saudacao que aceite um nome como argumento e imprima "Olá, [nome]!".'
    }

    if request.method == 'POST':
        nome = request.POST.get('nome')
        frase = f'Olá {nome}'
        data['frase'] = frase
    return render (request, 'ex19.html', data)


def ex20(request):
    data = {
        'titulo': 'Exercicio 20 Função de Soma',
        'descrição': 'Crie uma função chamada soma que receba dois números como parâmetros e retorne a soma desses dois números.'
    }

    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        total = int(valor1) + int(valor2)
        data['total'] = total
    return render(request, 'ex20.html', data)

def ex21(request):
    data = {
        'titulo': 'Exercicio 21 Função que Conta Caracteres',
        'descrição': 'Desenvolva uma função conta_caracteres que receba uma string como argumento e retorne o número de caracteres na string.'
    }

    if request.method == 'POST':
        palavra = request.POST.get("palavra") 
        if palavra:
            caracteres = len(palavra)
            data['caracteres'] = caracteres
        else:
            data['caracteres'] = 0  
    return render(request, 'ex21.html', data)

def ex22(request):
    data = {
        'titulo': 'Exercicio 22 Função para Concatenar Strings',
        'descrição': 'Faça uma função chamada concatena que receba duas strings, parte1 e parte2, como parâmetros, una-as em uma nova string e retorne essa nova string'
    }

    if request.method == 'POST':
        parte1 = request.POST.get("parte1") 
        parte2 = request.POST.get("parte2")
        nova_string = str(parte1) + " " + str(parte2)
        data['nova_string'] = nova_string
    return render (request, 'ex22.html', data)

def ex23(request):
    data = {
        'titulo': 'Exercicio 23 Função de Cálculo de Idade',
        'descrição': 'Escreva uma função chamada calcula_idade que receba o ano atual e o ano de nascimento, e retorne a idade da pessoa'
    }

    if request.method == 'POST':
        Ano_de_nascimento = request.POST.get("ano_de_nascimento") 
        ano_atual = 2024
        data_de_nascimento = int(ano_atual) - int(Ano_de_nascimento)
        data['data_de_nascimento'] = data_de_nascimento
    return render(request, 'ex23.html', data)

def ex24(request):
    data = {
        'titulo': 'Exercicio 24 Função de Troca de Valores',
        'descrição': 'Crie uma função chamada troca_valores que receba dois valores a e b como parâmetros, troque os valores entre eles e retorne ambos'
    }

    if request.method == 'POST':
        a = request.POST.get("a")
        b = request.POST.get("b")
        troca = a, b = b, a
        data['troca'] = troca
    return render(request, 'ex24.html', data)

def ex25(request):
    data = {
        'titulo': 'Exercicio 25 Função de Repetição de String',
        'descrição': 'Desenvolva uma função chamada repete_string que receba uma string frase e um número inteiro n, e retorne a string repetida n vezes'
    }

    if request.method == 'POST':
        frase = request.POST.get("frase") 
        frase1 = request.POST.get("frase1")
        frase2 = str(frase) * int(frase1)
        data['frase2'] = frase2
    return render(request, 'ex25.html', data)

def ex26(request):
    data = {
        'titulo': 'Exercicio 26 Função para Calcular Média',
        'descrição': 'Faça uma função chamada media que receba quatro números como argumentos e retorne a média desses números'
    }

    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        valor3 = request.POST.get("valor3") 
        valor4 = request.POST.get("valor4")
        media = (int(valor1) + int(valor2) + int(valor3) + int(valor4))/4
        data['media'] = media
    return render (request, 'ex26.html', data)

def ex27(request):
    data = {
        'titulo': 'Exercicio 27 Função para Descrição de Objetos Coloridos',
        'descrição': 'Crie uma função chamada descreve_cor que receba duas strings, cor e objeto, e retorne uma descrição do tipo "objeto cor"'
    }

    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " " + str(palavra1) + " " 
        data['frase'] = frase
    return render (request, 'ex27.html', data)

def ex28(request):
    data = {
        'titulo': 'Exercicio 28 Função para Descrição Geográfica',
        'descrição': 'Escreva uma função chamada posicao_geografica que receba os nomes de duas cidades e retorne uma frase indicando que a primeira cidade está a leste da segunda'
    }

    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " está a leste de " + str(palavra1)
        data['frase'] = frase
    return render(request, 'ex28.html', data)