class Cliente:
    __id = None
    __nome = None
    __cpf = None

    def __init__(self, id, nome, cpf):
        self.__id = id
        self.__nome = nome
        self.__cpf= cpf

    def getClientId(self):
        return self.__id

    def getClientNome(self):
        return self.__nome

      def getClientCpf(self):
        return self.__cpf

    def getClientName(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self.__nome
        else:
            retorno = "Cliente não encontrado!!"
        return(retorno)
