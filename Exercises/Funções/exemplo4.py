# Definindo o que eu gostaria de que ela fizesse quando chamada
def comprimenta():
    print("Olá")
    print("Boa tarde")
    print("Boa tarde Fulano")


def comprimenta2(nome):
    print("Olá, " + nome)
    print("Boa tarde " + nome)


# Chamada da função
comprimenta()


comprimenta2("Kaique")
comprimenta2("Gregory")
comprimenta2("Enzo")