import getpass
import hashlib

ras = []
emails = []
senhas = []

print("---)---  ---)---  ---)---  ---)--- ---)---  ---)---  ---)---    ---)--- ---)---  ---)---  ---)---  ---)--")
print(" --) ____ --  ___ -- ___    ___ ---)-________ ---)- ________ ---)-_________  ---)--- ---)-- ---)-- ---)--")
print(")---|    \---|   |--|   |  |   |--- /        \---)-|   __  \\---) /         \      ---)---  ---)--- ---)-")
print(" -- |     \--|   |--|   |  |   | --|    __    |--- |  |__|  ||-- |    __    | ---)---  ---)---  ---)----)")
print("---)|      \-|   |--|   |  |   |---|   |__|   | ---|   ____// ---|   |__|   |      ---)---  ---)--- ---)-")
print(")---|   |\  \|   |--|   |__|   |---|   |  |   |)---|   |---)--- -|   |  |   |  ---)---  ---)---  ---)----")
print("---)|   |-\      |---\        /---)|   |  |   |---)|   | ---)--- |   |  |   |       ---)--- ---)---  --)-")
print(")---|___|--\_____|----\______/---)-|___|  |___|-)--|___|---)---  |___|  |___|   ---)---  ---)---  ---)---")
print("---)---  ---)---  ---)---    ---)--- ---)---  ---)---  ---)---    ---)--- ---)---  ---)---  ---)--- ---)-")

def menu_inicial():
    while True:
        print("BEM VINDO AO NUAPA")
        print("Opção 1 - Cadastro")
        print("Opção 2 - Login")
        print("Opção 3 - Sair")
        opcao = int(input("Digite apenas o número da opção a qual deseja prosseguir: "))

        if opcao == 1:
            cadastro()
        elif opcao == 2:
            login()
        else:
            print("Retornando para o menu de opções..")

def cadastro():

    ra = input("Informe o seu RA, apenas em números: \n")
    email = input("Informe por gentileza o seu e-mail: \n")
    senha = getpass.getpass("Informe por gentileza qual será a sua senha: \n")
    confirmacao_senha = getpass.getpass("Confirme a senha inserida por gentileza: \n")

    while senha != confirmacao_senha:
        print("Senhas não coincidem. Por favor, digite novamente a confirmação de senha seguindo a senha inserida.")
        confirmacao_senha = input()

        if senha == confirmacao_senha:
            print("Senhas coincidem, prosseguindo para o cadastro...")
            break

    senha_hash = tratar_senha(str(senha))
    emails.append(email)
    ras.append(ra)
    senhas.append(senha_hash)

    print(f"Usuário com o RA: {ra} cadastrado com sucesso!")

def login():
    while True:
      valida_login = input("Olá, bem-vindo! Você já possui cadastro do sistema? Diga SIM para realizar o login, caso contrário, informe NÃO para realização do cadastro. \n").lower()
      valida_confirmacao = ['sim', 'ss', 's']

      if valida_login in valida_confirmacao:

        ra_login = input("Informe seu RA: \n")
        senha_login = getpass.getpass("Informe sua senha: \n")
        senha_hash = tratar_senha(senha_login)

        contador = 0
        while contador < len(ras) and contador < len(senhas):
          if ra_login == ras[contador] and senha_hash == senhas[contador]:
              central_app(ra_login)
              break
          contador += 1
        else:
            print("Usuário ou senha incorretos. Tente novamente!!!")

      else:
        print("Saindo do App Nuapa...")
        break

def central_app(ra_login):
  print(f"Login bem sucedido!!! Usuário {ra_login}, tendo permissões e acesso a serviços deste software.")

def tratar_senha(senha):

    hash_sha256 = hashlib.sha256()
    hash_sha256.update(senha.encode('utf8'))
    return hash_sha256.hexdigest()

def __init():
    menu_inicial()
__init()
