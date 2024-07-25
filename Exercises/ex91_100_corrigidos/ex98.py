class Pessoa:
    nome = ''
    sobrenome = ''
    idade = None
    profissao = ""


    def __init__(self, nome_passado, sobrenome_passado, idade_passada, profissao_passada):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.profissao = profissao_passada

    def modifica_nome(self, novo_nome):
        self.nome = novo_nome

    def modifica_sobrenome(self, novo_sobrenome):
        self.sobrenome = novo_sobrenome

    def imprime_dados_completos(self):
        return self.nome + self.sobrenome + str(self.idade) + self.profissao

pessoa = Pessoa("Kaique ", "Monteiro  ", 14, " estagiario ")
pessoa.modifica_nome("Marcelo ")
pessoa.modifica_sobrenome("Ferreira ")
print(pessoa.imprime_dados_completos())