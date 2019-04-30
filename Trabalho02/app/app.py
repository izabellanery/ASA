# Desenvolvido por:
#
# Izabella Guedes Pereira Nery      11611ECP015
# Murilo Rezende Montano            11611ECP011

from flask import Flask, url_for, request, json, jsonify
from json import dumps
from dbUtils import DbUtils


app = Flask(__name__)
#myUser = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!'

@app.route('/echo', methods = ['GET', 'POST'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET"

    elif request.method == 'POST':
        return "ECHO: POST"

# ------------------------- Criacao das tabelas ------------------------- #
#                                                                         #
# Ordem de criacao:                                                       #
#                                                                         #
#  - Categorias                                                           #
#  - Fornecedores                                                         #
#  - Vendedores                                                           #
#  - Produtos                                                             #
#  - Compras                                                              #
#  - Vendas                                                               #
# ----------------------------------------------------------------------- #
    
@app.route('/createdbcategorias')
def api_createdbcategorias():
    dbUtils = DbUtils()
    if (dbUtils.createTableCategorias()):
        result = {"result": "Tablea criada!"}
    else:
        result = {"result": "Problemas para criar a tabela!"}
    return jsonify(result)

@app.route('/createdbfornecedores')
def api_createdbfornecedores():
    dbUtils = DbUtils()
    if (dbUtils.createTableFornecedores()):
        result = {"result": "Tablea criada!"}
    else:
        result = {"result": "Problemas para criar a tabela!"}
    return jsonify(result)

@app.route('/createdbvendedores')
def api_createdbvendedores():
    dbUtils = DbUtils()
    if (dbUtils.createTableVendedores()):
        result = {"result": "Tablea criada!"}
    else:
        result = {"result": "Problemas para criar a tabela!"}
    return jsonify(result)

@app.route('/createdbprodutos')
def api_createdbprodutos():
    dbUtils = DbUtils()
    if (dbUtils.createTableProdutos()):
        result = {"result": "Tablea criada!"}
    else:
        result = {"result": "Problemas para criar a tabela!"}
    return jsonify(result)

@app.route('/createdbcompras')
def api_createdbcompras():
    dbUtils = DbUtils()
    if (dbUtils.createTableCompras()):
        result = {"result": "Tablea criada!"}
    else:
        result = {"result": "Problemas para criar a tabela!"}
    return jsonify(result)

@app.route('/createdbvendas')
def api_createdbvendas():
    dbUtils = DbUtils()
    if (dbUtils.createTableVendas()):
        result = {"result": "Tablea criada!"}
    else:
        result = {"result": "Problemas para criar a tabela!"}
    return jsonify(result)

# ------------------------- Categorias ------------------------- #

@app.route('/addcategoria', methods=['POST'])
def api_addcategoria():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    id_categoria = req_data['id_categoria']
    tituloCategoria = req_data['tituloCategoria']
    descricaoCategoria = req_data['descricaoCategoria']
    fg_ativo = req_data['fg_ativo']

    dbUtils = DbUtils()
        
    if(dbUtils.addCategoria(id_categoria, tituloCategoria, descricaoCategoria, fg_ativo)):
        result = {"result": "Categoria inserida com sucesso!"}
    else:
        result = {"result": "Problemas!"}

    return jsonify(result)

@app.route('/getcategorias')
def api_getcategorias():
    categorias = []
    dbUtils = DbUtils()
    categoriasData = dbUtils.getCategorias()
    for r in categoriasData:
        a = {"id_categoria": r[0], "tituloCategoria" : r[1], "descricaoCategoria": r[2], "fg_ativo" : r[3]}
        categorias.append(a)

    return jsonify(categorias)

# ------------------------- Fornecedores ------------------------- #

@app.route('/addfornecedor', methods=['POST'])
def api_addfornecedor():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    id_fornecedor = req_data['id_fornecedor']
    cnpj = req_data['cnpj']
    razaoSocial = req_data['razaoSocial']
    telefone = req_data['telefone']
    endereco = req_data['endereco']
    contato = req_data['contato']
    fg_ativo = req_data['fg_ativo']

    dbUtils = DbUtils()
        
    if(dbUtils.addFornecedor(id_fornecedor, cnpj, razaoSocial, telefone, endereco, contato, fg_ativo)):
        result = {"result": "Fornecedor inserido com sucesso!"}
    else:
        result = {"result": "Problemas!"}

    return jsonify(result)

@app.route('/getfornecedores')
def api_getfornecedores():
    fornecedores = []
    dbUtils = DbUtils()
    fornecedoresData = dbUtils.getFornecedores()
    for r in fornecedoresData:
        a = {"id_fornecedor": r[0], "cnpj" : r[1], "razaoSocial": r[2], "telefone" : r[3], "endereco" : r[4], "contato" : r[5], "fg_ativo" : r[6]}
        fornecedores.append(a)

    return jsonify(fornecedores)

# ------------------------- Vendedores ------------------------- #

@app.route('/addvendedor', methods=['POST'])
def api_addvendedor():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    id_vendedor = req_data['id_vendedor']
    cpf = req_data['cpf']
    nome = req_data['nome']
    carteiraTrabalho = req_data['carteiraTrabalho']
    telefone = req_data['telefone']
    dataAdmissao = req_data['dataAdmissao']
    fg_ativo = req_data['fg_ativo']

    dbUtils = DbUtils()
        
    if(dbUtils.addVendedor(id_vendedor, cpf, nome, carteiraTrabalho, telefone, dataAdmissao, fg_ativo)):
        result = {"result": "Vendedor inserido com sucesso!"}
    else:
        result = {"result": "Problemas!"}

    return jsonify(result)

@app.route('/getvendedores')
def api_getvendedores():
    vendedores = []
    dbUtils = DbUtils()
    vendedoresData = dbUtils.getVendedores()
    for r in vendedoresData:
        a = {"id_vendedor": r[0], "cpf" : r[1], "nome": r[2], "carteiraTrabalho": r[3], "telefone": r[4], "dataAdmissao" : r[5], "fg_ativo" : r[6]}
        vendedores.append(a)

    return jsonify(vendedores)

# ------------------------- Produtos ------------------------- #

@app.route('/addproduto', methods=['POST'])
def api_addproduto():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    id_produto = req_data['id_produto']
    id_fornecedor = req_data['id_fornecedor']
    id_categoria = req_data['id_categoria']
    nomeProduto = req_data['nomeProduto']
    descricaoProduto = req_data['descricaoProduto']
    valorUnitario = req_data['valorUnitario']
    quantidade = req_data['quantidade']
    quantidadeMinima = req_data['quantidadeMinima']
    fg_ativo = req_data['fg_ativo']

    dbUtils = DbUtils()
        
    if(dbUtils.addProduto(id_produto, id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima, fg_ativo)):
        result = {"result": "Produto inserido com sucesso!"}
    else:
        result = {"result": "Problemas!"}

    return jsonify(result)

@app.route('/getprodutos')
def api_getprodutos():
    produtos = []
    dbUtils = DbUtils()
    produtosData = dbUtils.getProdutos()
    for r in produtosData:
        a = {"id_produto": r[0], "id_fornecedor" : r[1], "id_categoria": r[2], "nomeProduto": r[3], "descricaoProduto": r[4], "valorUnitario" : r[5], "quantidade" : r[6], "quantidadeMinima" : r[7], "fg_ativo" : r[8]}
        produtos.append(a)

    return jsonify(produtos)

# ------------------------- Compras ------------------------- #

@app.route('/addcompra', methods=['POST'])
def api_addcompra():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    id_compra = req_data['id_compra']
    id_fornecedor = req_data['id_fornecedor']
    id_produto = req_data['id_produto']
    id_categoria = req_data['id_categoria']
    dataCompra = req_data['dataCompra']
    valorTotal = req_data['valorTotal']
    quantidade = req_data['quantidade']
    fg_ativo = req_data['fg_ativo']

    dbUtils = DbUtils()
        
    if(dbUtils.addCompra(id_compra, id_fornecedor, id_produto, id_categoria, dataCompra, valorTotal, quantidade, fg_ativo)):
        result = {"result": "Compra inserida com sucesso!"}
    else:
        result = {"result": "Problemas!"}

    return jsonify(result)

@app.route('/getcompras')
def api_getcompras():
    compras = []
    dbUtils = DbUtils()
    comprasData = dbUtils.getCompras()
    for r in comprasData:
        a = {"id_compra" : r[0], "id_fornecedor" : r[1], "id_produto": r[2], "id_categoria": r[3], "dataCompra": r[4], "valorTotal": r[5], "quantidade" : r[6], "fg_ativo" : r[7]}
        compras.append(a)

    return jsonify(compras)

# ------------------------- Vendas ------------------------- #

@app.route('/addvenda', methods=['POST'])
def api_addvenda():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    id_venda = req_data['id_venda']
    id_vendedor = req_data['id_vendedor']
    id_categoria = req_data['id_categoria']
    id_produto = req_data['id_produto']
    dataVenda = req_data['dataVenda']
    valorTotal = req_data['valorTotal']
    quantidade = req_data['quantidade']
    fg_ativo = req_data['fg_ativo']

    dbUtils = DbUtils()
        
    if(dbUtils.addVenda(id_venda, id_vendedor, id_categoria, id_produto, dataVenda, valorTotal, quantidade, fg_ativo)):
        result = {"result": "Venda inserida com sucesso!"}
    else:
        result = {"result": "Problemas!"}

    return jsonify(result)

@app.route('/getvendas')
def api_getvendas():
    vendas = []
    dbUtils = DbUtils()
    vendasData = dbUtils.getVendas()
    for r in vendasData:
        a = {"id_venda" : r[0], "id_vendedor" : r[1], "id_categoria": r[2], "id_produto": r[3], "dataVenda": r[4], "valorTotal": r[5], "quantidade" : r[6], "fg_ativo" : r[7]}
        vendas.append(a)

    return jsonify(vendas)

# -------------------------------------------------- #
    
if __name__ == '__main__':
    app.run()
