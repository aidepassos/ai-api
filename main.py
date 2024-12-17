from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json()  # Obtém os dados JSON enviados na requisição
        if data and 'name' in data:
            name = data['name']
            return jsonify({'message': f'Hello, {name}!'}), 200 # Retorna 200 Ok
        else:
            return jsonify({'error': 'Nome não fornecido no JSON'}), 400 # Retorna 400 Bad Request
    else: #request.method == 'GET'
        return jsonify({'message': 'Hello, Anonymous!'}), 200 #Retorna 200 Ok

if __name__ == '__main__':
    # app.run(debug=True)
    lista = ["Primeiro", ["Primeiro Interno", 911], 190]
    print(lista)
    print(f"Tamanho da lista {len(lista)}")
    indice = 1
    indice_interno = 1
    for item in lista:
        if isinstance(item, any):
            for item_interno in item:
                print(f"->Item interno {indice_interno} da lista interna: {item_interno} e seu tipo eh: {type(item_interno)}")
                indice_interno += 1
        elif isinstance(item, list):
            print(f"Item {indice} da lista: {item} e seu tipo eh: {type(item)}")
        indice += 1