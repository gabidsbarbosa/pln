from flask import Flask, request, jsonify
from translate import Translator
from flask_cors import CORS  # Para permitir acesso do frontend

app = Flask(__name__)
CORS(app)  # Permite chamadas do frontend

@app.route('/traduzir', methods=['POST'])
def traduzir_texto():
    dados = request.json
    texto = dados.get("texto", "")
    idioma = dados.get("idioma", "en")

    if not texto.strip():
        return jsonify({"erro": "Texto não pode estar vazio!"}), 400

    try:
        tradutor = Translator(to_lang=idioma)
        traducao = tradutor.translate(texto)
        return jsonify({"traducao": traducao})
    except Exception as e:
        return jsonify({"erro": f"Erro ao traduzir: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
