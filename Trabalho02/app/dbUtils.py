# Desenvolvido por:
#
# Izabella Guedes Pereira Nery      11611ECP015
# Murilo Rezende Montano            11611ECP011

from sqlalchemy import create_engine

class DbUtils:
    db_string = "postgresql+psycopg2://postgres:banco@localhost/asa"
    db_query = ""

    # ------------------------- Categorias ------------------------- #
    
    def createTableCategorias(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE loja.tb_categorias (id_categoria INTEGER PRIMARY KEY, tituloCategoria VARCHAR(100), descricaoCategoria VARCHAR(250), fg_ativo INTEGER);"
        
        try:
            db.execute(self.db_query)
            res = True
        except Exception as e:
            print("Problemas ao criar a tabela categorias\n" + str(e))
            res = False
        return res

    def addCategoria(self, id_categoria, tituloCategoria, descricaoCategoria, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO loja.tb_categorias(id_categoria, tituloCategoria, descricaoCategoria, fg_ativo) VALUES (%s, %s, %s, %s);", id_categoria, tituloCategoria, descricaoCategoria, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela categorias\n")
            res = False
        return res

    def getCategorias(self):
        db = create_engine(self.db_string)
        categorias = db.execute("SELECT * FROM loja.tb_categorias")
        return categorias

    # ------------------------- Fornecedores ------------------------- #
    
    def createTableFornecedores(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE loja.tb_fornecedores (id_fornecedor INTEGER PRIMARY KEY, cnpj VARCHAR(20), razaoSocial VARCHAR(100), telefone VARCHAR(13), endereco VARCHAR(250), contato VARCHAR(150), fg_ativo INTEGER); "
        
        try:
            db.execute(self.db_query)
            res = True
        except Exception as e:
            print("Problemas ao criar a tabela fornecedores\n" + str(e))
            res = False
        return res

    def addFornecedor(self, id_fornecedor, cnpj, razaoSocial, telefone, endereco, contato, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO loja.tb_fornecedores(id_fornecedor, cnpj, razaoSocial, telefone, endereco, contato, fg_ativo) VALUES (%s, %s, %s, %s, %s, %s, %s);", id_fornecedor, cnpj, razaoSocial, telefone, endereco, contato, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela fornecedores\n")
            res = False
        return res

    def getFornecedores(self):
        db = create_engine(self.db_string)
        fornecedores = db.execute("SELECT * FROM loja.tb_fornecedores")
        return fornecedores

    # ------------------------- Vendedores ------------------------- #

    def createTableVendedores(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE loja.tb_vendedores (id_vendedor INTEGER PRIMARY KEY, cpf VARCHAR(14), nome VARCHAR(150), carteiraTrabalho VARCHAR(100), telefone VARCHAR(13), dataAdmissao DATE, fg_ativo INTEGER);"
        
        try:
            db.execute(self.db_query)
            res = True
        except Exception as e:
            print("Problemas ao criar a tabela vendedores\n" + str(e))
            res = False
        return res
    
    def addVendedor(self, id_vendedor, cpf, nome, carteiraTrabalho, telefone, dataAdmissao, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO loja.tb_vendedores(id_vendedor, cpf, nome, carteiraTrabalho, telefone, dataAdmissao, fg_ativo) VALUES (%s, %s, %s, %s, %s, %s, %s);", id_vendedor, cpf, nome, carteiraTrabalho, telefone, dataAdmissao, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela vendedores\n")
            res = False
        return res

    def getVendedores(self):
        db = create_engine(self.db_string)
        vendedores = db.execute("SELECT * FROM loja.tb_vendedores")
        return vendedores

    # ------------------------- Produtos ------------------------- #

    def createTableProdutos(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE loja.tb_produtos (id_produto INTEGER PRIMARY KEY, id_fornecedor INTEGER, id_categoria INTEGER, nomeProduto VARCHAR(100), descricaoProduto VARCHAR(250), valorUnitario NUMERIC, quantidade INTEGER, quantidadeMinima INTEGER, fg_ativo INTEGER, FOREIGN KEY (id_fornecedor) REFERENCES loja.tb_fornecedores (id_fornecedor), FOREIGN KEY (id_categoria) REFERENCES loja.tb_categorias (id_categoria));"
        
        try:
            db.execute(self.db_query)
            res = True
        except Exception as e:
            print("Problemas ao criar a tabela produtos\n" + str(e))
            res = False
        return res

    def addProduto(self, id_produto, id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO loja.tb_produtos(id_produto, id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima, fg_ativo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", id_produto, id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela produtos\n")
            res = False
        return res

    def getProdutos(self):
        db = create_engine(self.db_string)
        produtos = db.execute("SELECT * FROM loja.tb_produtos")
        return produtos
    
    # ------------------------- Compras ------------------------- #

    def createTableCompras(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE loja.tb_compras (id_compra INTEGER PRIMARY KEY, id_fornecedor INTEGER, id_produto INTEGER, id_categoria INTEGER, dataCompra DATE, valorTotal NUMERIC, quantidade INTEGER, fg_ativo INTEGER, FOREIGN KEY (id_fornecedor) REFERENCES loja.tb_fornecedores (id_fornecedor), FOREIGN KEY (id_produto) REFERENCES loja.tb_produtos (id_produto), FOREIGN KEY (id_categoria) REFERENCES loja.tb_categorias (id_categoria));"
        
        try:
            db.execute(self.db_query)
            res = True
        except Exception as e:
            print("Problemas ao criar a tabela compras\n" + str(e))
            res = False
        return res

    def addCompra(self, id_compra, id_fornecedor, id_produto, id_categoria, dataCompra, valorTotal, quantidade, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO loja.tb_compras(id_compra, id_fornecedor, id_produto, id_categoria, dataCompra, valorTotal, quantidade, fg_ativo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", id_compra, id_fornecedor, id_produto, id_categoria, dataCompra, valorTotal, quantidade, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela compras\n")
            res = False
        return res

    def getCompras(self):
        db = create_engine(self.db_string)
        compras = db.execute("SELECT * FROM loja.tb_compras")
        return compras

    # ------------------------- Vendas ------------------------- #

    def createTableVendas(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE loja.tb_vendas (id_venda INTEGER PRIMARY KEY, id_vendedor INTEGER, id_categoria INTEGER, id_produto INTEGER, dataVenda DATE, valorTotal NUMERIC, quantidade INTEGER, fg_ativo INTEGER, FOREIGN KEY (id_vendedor) REFERENCES loja.tb_vendedores (id_vendedor), FOREIGN KEY (id_categoria) REFERENCES loja.tb_categorias (id_categoria), FOREIGN KEY (id_produto) REFERENCES loja.tb_produtos (id_produto));"
        
        try:
            db.execute(self.db_query)
            res = True
        except Exception as e:
            print("Problemas ao criar a tabela vendas\n" + str(e))
            res = False
        return res

    def addVenda(self, id_venda, id_vendedor, id_categoria, id_produto, dataVenda, valorTotal, quantidade, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO loja.tb_vendas(id_venda, id_vendedor, id_categoria, id_produto, dataVenda, valorTotal, quantidade, fg_ativo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", id_venda, id_vendedor, id_categoria, id_produto, dataVenda, valorTotal, quantidade, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela vendas\n")
            res = False
        return res

    def getVendas(self):
        db = create_engine(self.db_string)
        vendas = db.execute("SELECT * FROM loja.tb_vendas")
        return vendas

    # -------------------------------------------------- #
    
