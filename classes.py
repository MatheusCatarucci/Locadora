import os

class Locadora:
    # Método construtor
    def __init__(self):
        self.__clientes = {}
        self.__itens = {}

    # Métodos
    def cadastrarCliente(self, cliente):
        cpf = cliente.getCpf()
        if cpf in self.__clientes:
            os.system("cls")
            print("Usuário já cadastrado")
        else:
            self.__clientes[cpf] = cliente
    
    def cadastrarItem(self, item):
        id = item.getId()
        if id in self.__itens:
            os.system("cls")
            print("ID já cadastrado")
            os.system("pause")
        else:
            os.system("cls")
            self.__itens[id] = item
            print("Item cadastrado com suceso")

    def listarClientes(self, cliente):
        if not self.__clientes:
            os.system("cls")
            print("Nenhum cliente cadastrado")
            os.system("pause")
        else:
            os.system("cls")            
            for cpf, cliente in self.__clientes.items():
                print(f"Nome: {cliente.getNome()}")
                print(f"CPF: {cliente.getCpf()}")
                print("")
                print(20 * "=")
                print("")
                os.system("pause")

    def listarItens(self):
            if not self.__itens:
                os.system("cls")
                print("Nenhum item cadastrado")
            else:
                os.system("cls")
                disponibilidade = "DISPONÍVEL" if item.getDisponivel() else "INDISPONÍVEL" 
                for id, item in self.__itens.items():
                    print(f"ID: {item.getId()}")
                    print(f"Categoria: {item.getId()}")
                    print(f"Disponibilidade: {disponibilidade}")

                if isinstance(item, Jogo):
                    print(f"Plataforma: {item.getPlataforma()}")
                    print(f"Faixa Etária: {item.getFaixaEtaria()}")

                if isinstance(item, Filme):
                    print(f"Gênero: {item.getGenero()}")
                    print(f"Duração: {item.getDuracao()}")
            
                print("")
                print(20 * "=")
                print("")
            os.system("cls")

    def getItens(self):
        return self.__itens
    
    def getClientes(self):
        return self.__clientes

#================================================
class Cliente():
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

    # Métodos
    def locar(self, item):
        os.system("cls")
        if item.getDisponivel():
            self.__itensLocados.append(item)
            item.alugar()
            os.system("cls")
            print("Item alugado com sucesso")
            os.system("pause")
        else:
            os.system("cls")
            print("O item não esta disponível")
            os.system("pause")

    def devolver(self, item):
        if item in self.__itensLocados:
            self.__itensLocados.remove(item)
            item.devoler()
            print("Item removido com sucesso!")
        else:
            print("Este item não foi locado pelo cliente")

    def listarItens(self):
        if not self.__itensLocados:
            os.system("cls")
            print("Não há itens cadastrados")
            os.system("pause")
        else:
            for item in self.__itensLocados:
                print(f"Item: {item.getTitulo()}")
            

#================================================
class Item():
    _id_counter = 1

    def __init__(self, titulo, disponivel):
        self.__id = Item._id_counter
        self.__id_counter += 1
        self.__titulo = titulo
        self.__disponivel = disponivel

    # Getters e Setters
    def getId(self):
        return self.__id
    
    def getTitulo(self):
        return self.__titulo
    
    def getDisponivel(self):
        return self.__disponivel

    
    def setId(self, id):
        self.__id = id

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setDisponivel(self, disponivel):
        self.__disponivel = disponivel


    # Métodos
    def alugar(self):
        self.setDisponivel(False)
        return "Livro alugado com sucesso!"
    
    def devolver(self):
        self.setDisponivel(True)
        return "Livro devolvido com sucesso!"

#================================================
class Filme(Item):
    def __init__(self, titulo, disponivel, genero, duracao):
        super().__init__(titulo, disponivel)
        self.__genero = genero
        self.__duracao = duracao

    def getGenero(self):
        return self.__genero
    
    def getDuracao(self):
        return self.__duracao
    
    def setGenero(self, genero):
        self.__genero = genero

    def setDuracao(self, duracao):
        self.__duracao = duracao

#================================================
class Jogo(Item):
    def __init__(self, titulo, disponivel, plataforma, faixaEtaria):
        super().__init__(titulo, disponivel)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria
    
    def getPlataforma(self):
        return self.__plataforma
    
    def getFaixaEtaria(self):
        return self.__faixaEtaria

    def setPlataforma(self, plataforma):
        self.__plataforma = plataforma

    def setFaixaEtaria(self, faixaEtaria):
        self.__faixaEtaria = faixaEtaria
        