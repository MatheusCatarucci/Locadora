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