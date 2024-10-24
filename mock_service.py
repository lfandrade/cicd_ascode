from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/base/veracode/', methods=['POST'])
def veracode():
    return jsonify({"message": "Mocked Veracode service"}), 200

@app.route('/base/browserstack/', methods=['POST'])
def browserstack():
    return jsonify({"message": "Mocked BrowserStack service"}), 200

@app.route('/base/cyberark/chave', methods=['GET'])
def cyberark_chave():
    return jsonify({"message": "Mocked CyberArk chave"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)