from classes import *
import os

locadora = Locadora()

# ====================
# Funções auxiliares
# ====================
def limpar_tela():
    os.system("cls")


def pause():
    os.system("pause")


def listagem_locadora():
    limpar_tela()
    locadora.listarItens()


def registrar_itens():
    while True:
        limpar_tela()
        print("===== REGISTRO DE ITENS =====")
        print("1 - Jogos")
        print("2 - Filmes")
        print("0 - Voltar ao menu")
        escolha = int(input("--> "))
        match escolha:
            case 1:
                limpar_tela()
                print("0 para voltar\n")
                titulo = input("Qual o titulo do jogo?\n--> ")
                if titulo == "0":
                    continue
                limpar_tela()
                print("0 para voltar\n")
                plataforma = input("Qual a plataforma do jogo?\n--> ")
                if plataforma == "0":
                    continue
                limpar_tela()
                print("0 para voltar\n")
                faixaetaria = int(input("Faixa etária de quantos anos?\n--> "))
                if faixaetaria == 0:
                    continue
                limpar_tela()
                print("0 para voltar\n")
                disponivel_opcao = input(
                    "O jogo está disponível para troca? (s/n)\n--> "
                )
                limpar_tela()
                print("Jogo cadastrado com sucesso")
                pause()
                if disponivel_opcao == "s":
                    disponivel = True
                elif disponivel_opcao == "n":
                    disponivel = False
                else:
                    print("Opção inválida")
                    pause()
                jogo = Jogo(
                    titulo=titulo,
                    plataforma=plataforma,
                    faixaEtaria=faixaetaria,
                    disponivel=disponivel,
                )
                locadora.cadastrarItem(jogo)
            case 2:
                limpar_tela()
                print("0 para voltar\n")
                titulo = input("Qual o titulo do livro?\n--> ")
                limpar_tela()
                print("0 para voltar\n")
                genero = input("Qual o gênero do livro?\n--> ")
                limpar_tela()
                print("0 para voltar\n")
                duracao = input("Qual a duração do filme em minutos?\n--> ")
                limpar_tela()
                filme = Filme(titulo=titulo, genero=genero, duracao=duracao)
                locadora.cadastrarItem(filme)
            case 0:
                break
            case _:
                print("Opção inválida")
                pause()


def cadastro_clientes():
    while True:
        limpar_tela()
        print("Digite 0 pra sair\n")
        nome = input("Digite o nome do cliente\n--> ")
        if nome == "0":
            break
        cpf_input = input("Digite o CPF do usuário\n--> ")
        if cpf_input == "0":
            break
        if not cpf_input.isdigit():  # verifica se é só número
            print("CPF inválido! Digite apenas números.")
            pause()  # pausa a execução até o usuário pressionar uma tecla
            continue  # volta pro início do loop
        cpf = int(cpf_input)
        cliente = Cliente(nome, cpf)
        cliente.setNome()
        cliente.setCpf()
        print("Cliente cadastrado com sucesso")
        pause()


def menu():
    while True:
        limpar_tela()
        print(
            "Bem vindo a LOCADORA DO SENAI!\n1- Cadastrar cliente\n2- Registrar itens para locação\n3- Listagem de itens da locadora\n4- Controle de empréstimos\nEscolha uma opção\n"
        )
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
                listagem_locadora()
            case 4:
                pass
            case _:
                print("Opção inválida")
                pause()


menu()
