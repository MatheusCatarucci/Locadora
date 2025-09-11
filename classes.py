import os

class Locadora:
    # Método construtor
    def __init__(self):
        self.__clientes = {}
        self.__itens = {}

    # Métodos
    def cadastrarCliente(self, nome, cpf, cliente):
        if cpf in self.__clientes:
            print("Usuário já cadastrado!")
            os.system("pause")
        else:
            cpf = {
                "nome" : nome,
                "cpf" : cpf,
                "itens_locados": []
            }
        
        self.__clientes[cpf] = cliente
        print("Usuário cadastrado dcom sucesso!")
        os.system("pause")

    
    def cadastrarItem(self, item):
        self.__itens.append(item)
        print("Item cadastrado com sucesso!")

    def listarClientes(self):
        if not self.__clientes:
            print("Nenhum cliente cadastrado")
            os.system("pause")
        else:            
            for cliente in self.__clientes:
                print(f"Cliente: {cliente}")
            os.system("pause")

    def listarItens(self):
        if Item.getDisponivel():
            disponibilidade = "Disponível"
        else:
            disponibilidade = "Indisponível"
        if not self.__itens:
            print("Nenhum item cadastrado")
            os.system("pause")
        else:
            for item in self.__itens:
                print(f"ID: {item.getId()}, Título: {item.getTitulo()}, Disponível: {disponibilidade}")
            os.system("pause")

    def setClientes(self, clientes):
        self.__clientes = clientes

    def setItens(self, itens):
        self.__itens = itens

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
    _id_counter = 1

    def __init__(self, titulo, disponivel):
        self.__id = Item._id_counter
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

    # Getters e Setters
    def getTitulo(self):
        return super().getTitulo()
    
    def getDisponivel(self):
        return super().getDisponivel()
    
    def getPlataforma(self):
        return self.__plataforma
    
    def getFaixaEtaria(self):
        return self.__faixaEtaria
    
    def setTitulo(self):
        super().setTitulo()

    def setDisponivel(self):
        super().setDisponivel()

    def setPlataforma(self, plataforma):
        self.__plataforma = plataforma

    def setFaixaEtaria(self, faixaEtaria):
        self.__faixaEtaria = faixaEtaria