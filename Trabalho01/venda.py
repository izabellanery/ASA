class Venda:
    __idCliente = None
    __idProduto = None
    __quantidade = None
    __preco = None
    __total = None

    def __init__(self, idCliente, idProduto, quantidade, preco, total):
        self.__idCliente = idCliente
        self.__idProduto = idProduto
        self.__quantidade = quantidade
        self.__preco = preco
        self.__total = total

    def getClienteId(self):
        return self.__idCliente

    def getProdutoId(self):
        return self.__idProduto

    
    def getQuantidade(self):
        return self.__quantidade   

    
    def getTotal(self):
        return self.__total
