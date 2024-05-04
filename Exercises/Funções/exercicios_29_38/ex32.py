usuario_correto = "Kaique345"
senha_correta = "Kaique222"

nome_usuario = input("Digite nome de usuario: ")
senha = input("Digite senha: ")

if nome_usuario == usuario_correto and senha == senha_correta:
    print("Acesso concedido")
else:
    print("Acesso negado")