class Pessoa:
    nome = ''
    sobrenome = ''
    idade = None
    profissao = ""
    endereco = ""

    def __init__(self, nome_passado, sobrenome_passado, idade_passada, profissao_passada, endereco_passado):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.profissao = profissao_passada
        self.endereco = endereco_passado
    
    def imprimir_dados_completos(self,):
        return self.nome + self.sobrenome + self.profissao + str(self.idade)

pessoa1 = Pessoa("Kaique", " Monteiro ", 14, " estagiario ", " Rua geraldo Laranjeira numero 330")
pessoa2 = Pessoa("João ", "Gabriel ", 15 , "Programador ", " Rua 5 numero 110")
pessoa3 = Pessoa("Maria ", "Joaquina ", 23 , "Atriz ", "Rua 7 numero 490")

print(Pessoa.imprimir_dados_completos(pessoa1))
print(Pessoa.imprimir_dados_completos(pessoa2))
print(Pessoa.imprimir_dados_completos(pessoa3))