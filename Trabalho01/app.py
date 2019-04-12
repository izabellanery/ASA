from flask import Flask, url_for, request, json, jsonify
from cliente import Cliente
from produto import Produto
from venda import Venda

app = Flask(__name__)
myCliente = []
myProduto = []
myVenda = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'


@app.route('/creatcliente')
def api_creatclient():
    global myCliente
    myCliente.append(Cliente(1, "Joao", "111.111.111-11"))
    myCliente.append(Cliente(2, "Pedro", "222.222.222-22"))
    myCliente.append(Cliente(3, "Antonio", "333.333.333-33"))
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/addcliente', methods = ['POST'])
def api_newcliente():
    global myCliente
    req_data = request.get_json()

    id = req_data['id']
    nome = req_data['nome']
    cpf = req_data['cpf']
    
    new_cliente = Cliente(id, nome, cpf)
    myCliente.append(new_cliente)
    res = {'status':'ok'}
    return jsonify(res)

@app.route('/addproduto', methods = ['POST'])
def api_newProduto():
    global myProduto
    req_data = request.get_json()

    id = req_data['id']
    nome = req_data['nome']
    preco = req_data['preco']

    new_produto = Produto(id,nome,preco)
    myProduto.append(new_produto)
    res = {'status':'ok'}
    return jsonify(res)

 
@app.route('/venda', methods = ['POST'])
def api_newVenda():
    global myVenda

    req_data = request.get_json()

    idCliente = req_data['idCliente']
    idProduto = req_data['idProduto']
    quantidade = req_data['quantidade']
    preco = 0
    total = 0
    for elem in myProduto:
        if idProduto == elem.getIdProduto():
            preco = elem.getPrecoProduto()
            total = int(quantidade)*int(preco)
        else:
            print("Produto não esta cadastrado!!")
            break


    new_venda = Venda(idCliente,idProduto,quantidade,preco,str(total))
    myVenda.append(new_venda)
    res = {'status':'ok'}
    return jsonify(res)


@app.route('/vendacliente/<id_cliente>', methods = ['GET'])
def api_vendaCliente(id_cliente):
    cliente = id_cliente
    payload = []
    content = {}

    for elem in myVenda:
        if cliente == elem.getClientId():
            content = {'idCliente': str(elem.getClientId()),'[idProduto]': str(elem.getProdutoId()),
            '[quantidade]': elem.getQuantidade(), '[total]': elem.getTotal()}
            payload.append(content)
            content = {}
    
    res = json.dumps(payload)
    return jsonify(ListaVenda=res)
    
@app.route('/totalvendacliente/<id_cliente>', methods = ['GET'])
def api_totalvendaCliente(id_cliente):
    cliente = id_cliente
    payload = []
    content = {}
    total = 0

    for elem in myVenda:
        if cliente == elem.getClientId():
            total = total + int(elem.getTotal())
            content = {'idCliente': str(elem.getClientId()),'[totalGasto]': str(total)}
            payload.append(content)
            content = {}

    res = json.dumps(payload)
    return jsonify(ListaVenda=res)

@app.route('/listClientes', methods = ['GET'])
def api_listClientes():
    payload = []
    content = {}

    for elem in myCliente:
        content = {'id': str(elem.getClienteId()), '[nome]':elem.getClienteNome()}
        payload.append(content)
        content = {}

    res = json.dumps(payload)

    return jsonify(ListaCliente=res)

if __name__ == '__main__':
    app.run()

