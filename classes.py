class Locadora:
    # Método construtor
    def __init__(self):
        self.__clientes = []
        self.__itens = []

    # Métodos
    def cadastrarCliente(self, cliente):
        self.__clientes.append(cliente)
        print("Cliente Cadastrado com sucesso!")
    
    def cadastrarItem(self, item):
        self.__itens.append(item)
        print("Item cadastrado com sucesso!")

    def listarClientes(self):
        if not self.__clientes:
            print("Nenhum cliente cadastrado")
        else:            
            for cliente in self.__clientes:
                print(f"Cliente: {cliente}")

    def listarItens(self):
        if not self.__itens:
            print("Nenhum item cadastrado")
        else:
            for item in self.__itens:
                print(f"Item: {item}")

    def setClientes(self, clientes):
        self.__clientes = clientes

    def setItens(self, itens):
        self.__itens = itens

    def getItens(self):
        return self.__itens
    
    def getClientes(self):
        return self._clientes

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
    
    def setNome(self, nome):
        self.__nome = nome

    def setCpf(self, cpf):
        self.__cpf = cpf

    def setItensLocados(self, itensLocados):
        self.__itensLocados = itensLocados

    # Métodos
    def locar(self, item):
        self.__itensLocados.append(item)

    def devolver(self, item):
        if item in self.__itensLocados:
            self.__itensLocados.remove(item)
            print("Item removido com sucesso!")

    def listarItens(self):
        for item in self.__itensLocados:
            print(item)

#================================================
class Item():
    def __init__(self, titulo, disponivel):
        self.__id = 1
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

    def setDuracao(self, genero):
        self.__genero = genero

#================================================
class Jogo(Item):
    def __init__(self, titulo, disponivel, plataforma, faixaEtaria):
        super().__init__(titulo, disponivel)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria

    # Getters e Setters
    def getTitulo(self):
        return self.__titulo
    
    def getDisponivel(self):
        return self.__disponivel
    
    def getPlataforma(self):
        return self.__plataforma
    
    def getFaixaEtaria(self):
        return self.__faixaEtaria
    
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setDisponivel(self, disponivel):
        self.__disponivel = disponivel

    def setPlataforma(self, plataforma):
        self.__plataforma = plataforma

    def setFaixaEtaria(self, faixaEtaria):
        self.__faixaEtaria = faixaEtaria