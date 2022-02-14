from flask import Flask, request
import datetime
import json

app = Flask(__name__)

pedidos_json = {}

#construindo as funcionalidades  
@app.route('/')
def get_pedidos():
    with open("./pedidos.json", encoding="utf-8") as file:
        pedidos_json = json.load(file)
    return pedidos_json

@app.route('/add', methods=["POST"])
def add_pedido():
    pedido = request.get_json()

    with open ("pedidos.json", encoding="utf-8") as file:
        pedidos_json = json.load(file)
        pedidos = pedidos_json['pedidos']

        current_id = int(pedidos[-1]['id']) + 1
        timestamp = datetime.datetime.now()
        pedido['id'] = current_id
        pedido['timestamp'] = str(timestamp)
        pedidos.append(pedido)
        pedidos_json['pedidos'] = pedidos

    with open('pedidos.json', 'w', encoding="utf-8") as out_file:
        json.dump(pedidos_json, out_file, ensure_ascii=False)

    return pedido


@app.route('/edit/<id>', methods=['PUT'])
def edit_pedidos(id):
    pedido_alterado = request.get_json()

    def altera_pedido_se_for_o_que_eu_quero(pedido):
        if pedido and pedido['id'] == int(id) :
            pedido['cliente'] = pedido_alterado['cliente'] 
            pedido['produto'] = pedido_alterado['produto'] 
            pedido['valor'] = pedido_alterado['valor'] 
           
        return pedido

    with open("pedidos.json", encoding="utf-8") as file:
        pedidos_json = json.load(file)
        pedidos = pedidos_json['pedidos']
        if not any(pedido and pedido['id'] == int(id) for pedido in pedidos):

            return {'status': 400 }

        pedidos = list(map(altera_pedido_se_for_o_que_eu_quero, pedidos))
        pedidos_json['pedidos'] = pedidos

    with open('pedidos.json', 'w' ,encoding="utf-8") as out_file:
        json.dump(pedidos_json, out_file, ensure_ascii=False)

    return { 'status': 200 }

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_pedidos(id):

    with open("pedidos.json", encoding="utf-8") as file:
        pedidos_json = json.load(file)
        pedidos = [pedido if int(pedido['id']) != id else None for pedido in pedidos_json['pedidos'] if pedido != None]
        pedidos_json['pedidos'] = pedidos

    with open('pedidos.json', 'w' ,encoding="utf-8") as out_file:
      json.dump(pedidos_json, out_file, ensure_ascii=False)

    return { 'status': 200 }

#rodando a api

app.run()