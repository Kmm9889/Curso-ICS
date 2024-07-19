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

    def retorna_endeco(self):
        return self.endereco
    
pessoa = Pessoa("Kaique", "Monteiro", 14, "estagiario", "Rua geraldo Laranjeira numero 330")
print(pessoa.retorna_endeco())
