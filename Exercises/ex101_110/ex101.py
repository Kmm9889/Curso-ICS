class Pessoa:
    nome = None
    idade = None

    def __init__(self, nome_passado, idade_passada):
        self.nome = nome_passado
        self.idade = idade_passada

class Estudante(Pessoa):
    matricula = None

    def add_info_estudante(self, matricula_passada):
        self.matricula = matricula_passada

    def exibir_informacoes(self):
        return self.nome + str(self.idade) + self.matricula
    
estudante = Estudante("kaique ", 14,)
estudante.add_info_estudante(" Universidade Federal de Minas Gerais")
exibir_informacoes = estudante.exibir_informacoes()
print(exibir_informacoes)
