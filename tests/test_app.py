import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pytest
from app import app, PRED_FILE

# Función auxiliar para limpiar el archivo antes de cada prueba
def limpiar_predicciones():
    with open(PRED_FILE, 'w') as f:
        json.dump([], f)

# --------------------------
# PRUEBA 1: Categorías esperadas (parametrizada)
# --------------------------

@pytest.mark.parametrize(
    "frecuencia_cardiaca, nivel_glucosa, presion_sistolica, estado_esperado",
    [
        (50, 50, 50, "NO ENFERMO"),              # suma = 150
        (100, 80, 70, "ENFERMEDAD LEVE"),        # suma = 250
        (150, 100, 100, "ENFERMEDAD AGUDA"),     # suma = 350
        (200, 150, 100, "ENFERMEDAD CRÓNICA"),   # suma = 450
        (250, 200, 100, "ENFERMEDAD TERMINAL"),  # suma = 550
        (300, 300, 100, "ESTADO DESCONOCIDO")    # suma = 700
    ]
)
def test_prediccion_estado_parametrizada(frecuencia_cardiaca, nivel_glucosa, presion_sistolica, estado_esperado):
    """
    Prueba que cada conjunto de parámetros retorne la categoría de enfermedad esperada.
    """
    limpiar_predicciones()
    cliente = app.test_client()

    respuesta = cliente.post('/predecir', json={
        "frecuencia_cardiaca": frecuencia_cardiaca,
        "nivel_glucosa": nivel_glucosa,
        "presion_sistolica": presion_sistolica
    })

    assert respuesta.status_code == 200
    data = respuesta.get_json()
    assert data["estado"] == estado_esperado

# --------------------------
# PRUEBA 2: Verificar que el reporte se actualiza
# --------------------------

def test_reporte_refleja_ultima_prediccion():
    """
    Realiza una predicción y luego valida que /reporte
    refleje el estado correcto como último y en el conteo.
    """
    limpiar_predicciones()
    cliente = app.test_client()

    entrada = {
        "frecuencia_cardiaca": 120,
        "nivel_glucosa": 100,
        "presion_sistolica": 130
    }  # suma = 350 → ENFERMEDAD AGUDA

    cliente.post('/predecir', json=entrada)

    respuesta = cliente.get('/reporte')
    assert respuesta.status_code == 200
    reporte = respuesta.get_json()

    assert "ENFERMEDAD AGUDA" in reporte["conteo_por_estado"]
    assert reporte["conteo_por_estado"]["ENFERMEDAD AGUDA"] == 1
    assert reporte["fecha_ultima_prediccion"] is not None
    assert len(reporte["ultimas_5_predicciones"]) >= 1
    assert reporte["ultimas_5_predicciones"][-1]["estado"] == "ENFERMEDAD AGUDA"
