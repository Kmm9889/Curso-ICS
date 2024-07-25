from Estudante import Estudante

estudante = Estudante("Estudante", " De Programação ",  19, " Estudante", " Rua geraldo Laranjeira numero 330" )


estudante.altera_curso("Analise e desenvolvimento de sistemas")

print(estudante.imprimir_nome_completo())
print(estudante.retorna_curso())