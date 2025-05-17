from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
PRED_FILE = 'predicciones.json'

# Inicializar archivo si no existe
if not os.path.exists(PRED_FILE):
    with open(PRED_FILE, 'w') as f:
        json.dump([], f)

@app.route('/predecir', methods=['POST'])
def predecir():
    datos = request.get_json()
    frecuencia_cardiaca = datos.get("frecuencia_cardiaca", 0)
    nivel_glucosa = datos.get("nivel_glucosa", 0)
    presion_sistolica = datos.get("presion_sistolica", 0)

    resultado = predecir_estado(frecuencia_cardiaca, nivel_glucosa, presion_sistolica)

    # Guardar la predicción
    nueva_prediccion = {
        "estado": resultado,
        "fecha": datetime.now().isoformat()
    }

    with open(PRED_FILE, 'r+') as f:
        predicciones = json.load(f)
        predicciones.append(nueva_prediccion)
        f.seek(0)
        json.dump(predicciones, f, indent=2)

    return jsonify({"estado": resultado})

@app.route('/reporte', methods=['GET'])
def report():
    with open(PRED_FILE, 'r') as f:
        predicciones = json.load(f)

    conteo = {}
    for pred in predicciones:
        estado = pred["estado"]
        conteo[estado] = conteo.get(estado, 0) + 1

    ultimas_5 = predicciones[-5:]
    fecha_ultima = predicciones[-1]["fecha"] if predicciones else None

    return jsonify({
        "conteo_por_estado": conteo,
        "ultimas_5_predicciones": ultimas_5,
        "fecha_ultima_prediccion": fecha_ultima
    })

def predecir_estado(frecuencia_cardiaca, nivel_glucosa, presion_sistolica):
    suma = frecuencia_cardiaca + nivel_glucosa + presion_sistolica

    if suma < 200:
        return "NO ENFERMO"
    elif 200 <= suma < 300:
        return "ENFERMEDAD LEVE"
    elif 300 <= suma < 400:
        return "ENFERMEDAD AGUDA"
    elif 400 <= suma < 500:
        return "ENFERMEDAD CRÓNICA"
    elif 500 <= suma < 600:
        return "ENFERMEDAD TERMINAL"
    else:
        return "ESTADO DESCONOCIDO"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

