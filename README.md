# Diagnóstico Médico Automatizado

Este proyecto simula un diagnóstico médico utilizando reglas simples y una API construida con Flask. Permite a un usuario enviar tres valores clínicos y recibir un diagnóstico automático.

## Objetivo

Facilitar el despliegue de un modelo simulado de diagnóstico médico mediante contenedores Docker, sin requerir entornos complejos.

## Parámetros de entrada

La API recibe tres valores numéricos en formato JSON:

- `frecuencia_cardiaca` (ppm)  
- `nivel_glucosa` (mg/dL)  
- `presion_sistolica` (mm Hg)

Con base en estos, retorna uno de los siguientes diagnósticos:

- NO ENFERMO  
- ENFERMEDAD LEVE  
- ENFERMEDAD AGUDA  
- ENFERMEDAD CRÓNICA

## Estructura del proyecto

- `app.py`: expone la API con Flask  
- `modelo.py`: contiene la lógica del diagnóstico  
- `Dockerfile`: define la imagen Docker  
- `requirements.txt`: dependencias necesarias  
- `README.md`: documentación del proyecto