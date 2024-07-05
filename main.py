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
            # Capturando parâmetros do corpo (assumindo JSON)
            if request.is_json:
                body_params = request.get_json()
                print("JSON Body:", body_params)
            else:
                body_params = request.form.to_dict()
                print("Form Body:", body_params)

            # Retornando os parâmetros do corpo como JSON
            return jsonify(body_params), 200
        except Exception as e:
            print(f"Error processing POST request: {e}")
            return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run(debug=True)
