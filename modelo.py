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

