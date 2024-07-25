
class Pessoa:

    nome = ''
    quantidade = 0
    
    def __init__(self, nome):
        self.nome = nome
        Pessoa.quantidade += 1 
    
    def quantidade_pessoas():
        return Pessoa.quantidade

pessoa1 = Pessoa("Alice")
pessoa2 = Pessoa("Bob")
pessoa3 = Pessoa("Charlie")

print(Pessoa.quantidade_pessoas())