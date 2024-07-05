from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    # Capturando parâmetros de query
    query_params = request.args.to_dict()
    
    # Capturando parâmetros do corpo (assumindo JSON)
    if request.is_json:
        body_params = request.get_json()
    else:
        body_params = request.form.to_dict()
    
    # Combinando todos os parâmetros em um único dicionário
    combined_params = {
        'query_params': query_params,
        'body_params': body_params
    }
    
    # Retornando os parâmetros como JSON
    return jsonify(combined_params)

if __name__ == '__main__':
    app.run(debug=True)
