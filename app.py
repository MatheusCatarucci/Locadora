from classes import *

locadora = Locadora()

def registrar_itens():
    while True:
        limpar_tela()
        print("===== REGISTRO DE ITENS =====")
        print("1 - Jogos")
        print("2 - Filmes")
        print("0 - Voltar ao menu")

        try:
            escolha = int(input("--> "))
        except ValueError:
            print("Ocorreu um erro inesperado")
            pause()
            continue

        match escolha:
            case 1:
                limpar_tela()
                titulo = input("Título do jogo (0 para voltar): ")
                if titulo == "0": continue
                plataforma = input("Plataforma (0 para voltar): ")
                if plataforma == "0": continue

                try:
                    faixaetaria = int(input("Faixa etária: "))
                except ValueError:
                    print("Ocorreu um erro inesperado")
                    pause()
                    continue

                disponivel_opcao = input("Está disponível? (s/n): ").lower()
                disponivel = True if disponivel_opcao == "s" else False

                jogo = Jogo(titulo, plataforma, faixaetaria, disponivel)
                locadora.cadastrarItem(jogo)

            case 2:
                limpar_tela()
                titulo = input("Título do filme (0 para voltar): ")
                if titulo == "0": continue
                genero = input("Gênero: ")
                duracao = input("Duração em minutos: ")

                filme = Filme(titulo, genero, duracao)
                locadora.cadastrarItem(filme)

            case 0:
                break
            case _:
                print("Opção inválida")
                pause()


def cadastro_clientes():
    while True:
        limpar_tela()
        print("===== CADASTRO DE CLIENTES =====")
        nome = input("Nome do cliente (0 para sair): ")
        if nome == "0": break

        cpf_input = input("CPF (somente números, 0 para sair): ")
        if cpf_input == "0": break

        if not cpf_input.isdigit():
            print("CPF inválido! Digite apenas números.")
            pause()
            continue

        cpf = int(cpf_input)
        cliente = Cliente(nome, cpf)
        locadora.cadastrarCliente(cliente)


def menu():
    while True:
        limpar_tela()
        print("===== LOCADORA DO SENAI =====")
        print("1- Cadastrar cliente")
        print("2- Registrar itens")
        print("3- Listagem de itens")
        print("4- Listagem de clientes")
        print("0- Sair")

        try:
            escolha = int(input("--> "))
        except ValueError:
            print("Ocorreu um erro inesperado")
            pause()
            continue

        match escolha:
            case 1:
                cadastro_clientes()
            case 2:
                registrar_itens()
            case 3:
                locadora.listarItens()
            case 4:
                locadora.listarClientes()
            case 0:
                break
            case _:
                print("Opção inválida")
                pause()


menu()
