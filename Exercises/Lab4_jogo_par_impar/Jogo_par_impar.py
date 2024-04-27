def par_impar(valor):
    lista_impar = "1,3,5,7,9"
    ultimo_digito = valor[-1]

    if ultimo_digito in lista_impar:
         return "impar"
    else:
         return "par"
    
while True:
     valor = input("Digite um numero para descobrir se e par ou impar: ")
     res = par_impar(valor)
     print(res)
