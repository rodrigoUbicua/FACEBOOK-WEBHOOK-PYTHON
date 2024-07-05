from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = 'testando'

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'GET':
        # Verificação do webhook
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode and token:
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print('WEBHOOK_VERIFIED')
                return challenge, 200
            else:
                return 'Forbidden', 403
    elif request.method == 'POST':
        try:
            # Capturando parâmetros de query
            query_params = request.args.to_dict()
            
            # Capturando parâmetros do corpo (assumindo JSON)
            if request.is_json:
                body_params = request.get_json()
                print("JSON Body:", body_params)
            else:
                body_params = request.form.to_dict()
                print("Form Body:", body_params)
            
            # Combinando todos os parâmetros em um único dicionário
            combined_params = {
                'query_params': query_params,
                'body_params': body_params
            }
            
            # Retornando os parâmetros como JSON
            print("Combined Params:", combined_params)
            return jsonify(combined_params), 200
        except Exception as e:
            print(f"Error processing POST request: {e}")
            return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run(debug=True)
