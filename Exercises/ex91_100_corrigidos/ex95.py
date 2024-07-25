from Pessoa import  Pessoa

pessoa1 = Pessoa("Kaique", " Monteiro ", 14, " estagiario ", " Rua geraldo Laranjeira numero 330")
pessoa2 = Pessoa("João ", "Gabriel ", 15 , " Programador ", " Rua 5 numero 110")
pessoa3 = Pessoa("Maria ", "Joaquina ", 23 , " Atriz ", "Rua 7 numero 490")

lista = [pessoa1, pessoa2, pessoa3]

for pessoa in lista:
    print(pessoa.imprimir_dados_completos())

