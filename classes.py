import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPressione ENTER para continuar...")

class Locadora:
    def __init__(self):
        self.__clientes = {}
        self.__itens = {}

    def cadastrarCliente(self, cliente):
        cpf = cliente.getCpf()
        if cpf in self.__clientes:
            limpar_tela()
            print("Usuário já cadastrado")
            pause()
        else:
            self.__clientes[cpf] = cliente
            limpar_tela()
            print("Cliente cadastrado com sucesso!")
            pause()
    
    def cadastrarItem(self, item):
        id = item.getId()
        if id in self.__itens:
            limpar_tela()
            print("ID já cadastrado")
            pause()
        else:
            self.__itens[id] = item
            limpar_tela()
            print("Item cadastrado com sucesso")
            pause()

    def listarClientes(self):
        limpar_tela()
        if not self.__clientes:
            print("Nenhum cliente cadastrado")
        else:
            for cpf, cliente in self.__clientes.items():
                print(f"Nome: {cliente.getNome()}")
                print(f"CPF: {cliente.getCpf()}")
                print("=" * 20)
        pause()

    def listarItens(self):
        limpar_tela()
        if not self.__itens:
            print("Nenhum item cadastrado")
        else:
            for id, item in self.__itens.items():
                disponibilidade = "DISPONÍVEL" if item.getDisponivel() else "INDISPONÍVEL"
                print(f"ID: {item.getId()}")
                print(f"Título: {item.getTitulo()}")
                print(f"Disponibilidade: {disponibilidade}")

                if isinstance(item, Jogo):
                    print(f"Plataforma: {item.getPlataforma()}")
                    print(f"Faixa Etária: {item.getFaixaEtaria()}")

                if isinstance(item, Filme):
                    print(f"Gênero: {item.getGenero()}")
                    print(f"Duração: {item.getDuracao()} min")

                print("=" * 20)
        pause()

    def getItens(self):
        return self.__itens
    
    def getClientes(self):
        return self.__clientes


# =================================================
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = []

    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    def getItensLocados(self):
        return self.__itensLocados

    def locar(self, item):
        limpar_tela()
        if item.getDisponivel():
            self.__itensLocados.append(item)
            item.alugar()
            print("Item alugado com sucesso")
        else:
            print("O item não está disponível")
        pause()

    def devolver(self, item):
        limpar_tela()
        if item in self.__itensLocados:
            self.__itensLocados.remove(item)
            item.devolver()
            print("Item devolvido com sucesso!")
        else:
            print("Este item não foi locado pelo cliente")
        pause()

    def listarItens(self):
        limpar_tela()
        if not self.__itensLocados:
            print("Não há itens locados")
        else:
            for item in self.__itensLocados:
                print(f"Item: {item.getTitulo()}")
        pause()


# =================================================
class Item:
    _id_counter = 1

    def __init__(self, titulo, disponivel=True):
        self.__id = Item._id_counter
        Item._id_counter += 1
        self.__titulo = titulo
        self.__disponivel = disponivel

    def getId(self):
        return self.__id
    
    def getTitulo(self):
        return self.__titulo
    
    def getDisponivel(self):
        return self.__disponivel

    def setDisponivel(self, disponivel):
        self.__disponivel = disponivel

    def alugar(self):
        self.setDisponivel(False)
    
    def devolver(self):
        self.setDisponivel(True)


# =================================================
class Filme(Item):
    def __init__(self, titulo, genero, duracao, disponivel=True):
        super().__init__(titulo, disponivel)
        self.__genero = genero
        self.__duracao = duracao

    def getGenero(self):
        return self.__genero
    
    def getDuracao(self):
        return self.__duracao


# =================================================
class Jogo(Item):
    def __init__(self, titulo, plataforma, faixaEtaria, disponivel=True):
        super().__init__(titulo, disponivel)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria
    
    def getPlataforma(self):
        return self.__plataforma
    
    def getFaixaEtaria(self):
        return self.__faixaEtaria
