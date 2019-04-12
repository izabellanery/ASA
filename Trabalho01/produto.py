class Produto:
    __id = None
    __nome = None
    __preco = None

    def __init__(self, id, nome, preco):
        self.__id = id
        self.__nome = nome
        self.__preco = preco

    def getIdProduto(self):
        return self.__id

    def getNomeProduto(self):
        return self.__nome

    def getPrecoProduto(self):
        return self.__preco

    def getNomeProduto(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self.__nome
        else:
            retorno = "Produto não encontrado!!"
        return(retorno)

 
