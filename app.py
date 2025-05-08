from flask import Flask, request, jsonify
from modelo import predecir_estado

app = Flask(__name__)

@app.route('/predecir', methods=['POST'])
def predecir():
    datos = request.get_json()
    frecuencia_cardiaca = datos.get("frecuencia_cardiaca", 0)
    nivel_glucosa = datos.get("nivel_glucosa", 0)
    presion_sistolica = datos.get("presion_sistolica", 0)

    resultado = predecir_estado(frecuencia_cardiaca, nivel_glucosa, presion_sistolica)
    return jsonify({"estado": resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

