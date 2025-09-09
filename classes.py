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


#===============================================
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
        self.__itensLocados.append(item)

    def devolver(self, item):
        if item in self.__itensLocados:
            self.__itensLocados.remove(item)
            print("Item removido com sucesso!")

    # Métodos
    def listarItens(self):
        for item in self.__itensLocados:
            print(item)