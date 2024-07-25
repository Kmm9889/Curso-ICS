class Pessoa:
    nome = ""
    sobrenome = ""

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def criar_pessoa_anonima(self):
        return self.nome + self.sobrenome

pessoa1 = Pessoa("Anônimo ", "Silva")
print(pessoa1.criar_pessoa_anonima())
