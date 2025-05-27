# Diagnóstico Médico Automatizado

Este proyecto simula un sistema de diagnóstico médico basado en reglas simples. El objetivo es exponer un modelo simulado mediante una API para que un médico pueda ingresar tres valores clínicos y recibir un diagnóstico automatizado.

## Objetivo

Permitir el despliegue sencillo de un “modelo” simulado de diagnóstico usando contenedores Docker para el entregable 1, facilitando su uso sin necesidad de entornos de programación complejos.

## Los Parámetros de entrada

La función de diagnóstico requiere **tres valores numéricos** que representan mediciones clínicas. Estos deben ingresarse en una solicitud POST en formato JSON:

- `frecuencia_cardiaca`: Ritmo cardíaco en pulsaciones por minuto.
- `nivel_glucosa`: Nivel de glucosa en sangre 
- `presion_sistolica`: Presión sistólica

Estos valores serán evaluados mediante reglas simples para retornar un diagnóstico entre:

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA
- ENFERMEDAD TERMINAL

## Componentes del proyecto

- `app.py`: Archivo principal que expone el servicio mediante Flask.
- `Dockerfile`: Imagen personalizada que permite ejecutar el servicio.
- `requirements.txt`: Dependencias necesarias (Flask).
- `README.md`: Este archivo con información explicativa.

## Estructura del proyecto

```
Cristian-Gonzalez-mlops-U2/
├── app.py                      # Exposición del servicio mediante Flask
├── Dockerfile                  # Imagen personalizada de Docker
├── requirements.txt            # Dependencias necesarias
├── README.md                   # Este archivo con documentación del proyecto
├── Changelogs.docx             # Este archivo contiene los cambios en la propuesta del pipeline v2 vs v1
├── diagrama-v1.png             # La imagen del pipeline propuesto en la entrega 1
├── diagrama-v2.png             # la imagen del pipeline ajustado para la entrega 3
├── diseño-pipeline-V1.docx     # propuesta del pipeline enviado en la entrega 1
├── diseño-pipeline-V2.docx     # propuesta del pipeline ajustado para la entrega 3
```

## Despliegue con Docker

### 1. Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/crisdago18/Cristian-Gonzalez-mlops-U2
cd Cristian-Gonzalez-mlops-U2
```

Reemplaza la URL con la de tu propio repositorio en GitHub si es diferente.

2. Construir la imagen de Docker
Dentro del directorio del proyecto, ejecuta el siguiente comando para construir la imagen Docker:

```bash
docker build -t diagnostico-medico .
```

Este comando crea una imagen llamada diagnostico-medico utilizando el archivo Dockerfile del proyecto. Todas las dependencias necesarias serán instaladas automáticamente a través de requirements.txt.

 El tiempo de construcción puede variar dependiendo de los recursos del sistema y la velocidad de conexión.

3. Ejecutar el contenedor Docker
Una vez construida la imagen, ejecuta el siguiente comando para iniciar el servicio:

```bash
docker run -p 5000:5000 diagnostico-medico
```

Este comando inicia el contenedor y expone el servicio en el puerto 5000 de tu máquina.
Una vez en ejecución, el punto de acceso para las predicciones estará disponible en:

```bash
http://localhost:5000/predecir
```

## Prueba del servicio

### 1. Ejecutar la predicción

Usa el siguiente comando en tu terminal para enviar una solicitud `POST` al servicio:

```bash
curl -X POST http://localhost:5000/predecir \
-H "Content-Type: application/json" \
-d '{
  "frecuencia_cardiaca": 85,
  "nivel_glucosa": 105,
  "presion_sistolica": 115
}'
```

El servicio responderá con un JSON como el siguiente:

```json
{
  "estado": "ENFERMEDAD LEVE"
}
```

Esto indica que el contenedor y el servicio están funcionando correctamente.

### 2. Consultar el reporte de predicciones

Para ver un resumen de las predicciones realizadas, ejecuta el siguiente comando GET:

```bash
curl -X GET http://localhost:5000/report
```

El servicio responderá con un JSON como el siguiente:

```json
{
    "conteo_por_estado": {
        "ENFERMEDAD AGUDA": 2,
        "ENFERMEDAD TERMINAL": 2,
        "ENFERMEDAD GRAVE": 1
    },
    "fecha_ultima_prediccion": "2025-05-17T18:18:14.170791",
    "ultimas_5_predicciones": [
        {
            "estado": "ENFERMEDAD AGUDA",
            "fecha": "2025-05-17T18:04:26.703143"
        },
        {
            "estado": "ENFERMEDAD TERMINAL",
            "fecha": "2025-05-17T18:05:30.177223"
        },
        {
            "estado": "ENFERMEDAD AGUDA",
            "fecha": "2025-05-17T18:17:57.455637"
        },
        {
            "estado": "ENFERMEDAD TERMINAL",
            "fecha": "2025-05-17T18:18:04.591300"
        },
        {
            "estado": "ENFERMEDAD GRAVE",
            "fecha": "2025-05-17T18:18:14.170791"
        }
    ]
}
```