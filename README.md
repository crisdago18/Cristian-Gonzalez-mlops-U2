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

## Componentes del proyecto

- `app.py`: Archivo principal que expone el servicio mediante Flask.
- `modelo.py`: Contiene la lógica de diagnóstico simulada.
- `Dockerfile`: Imagen personalizada que permite ejecutar el servicio.
- `requirements.txt`: Dependencias necesarias (Flask).
- `README.md`: Este archivo con información explicativa.

## Estructura del proyecto

```
entregable_1/
├── app.py                # Exposición del servicio mediante Flask
├── modelo.py             # Lógica del diagnóstico simulado
├── Dockerfile            # Imagen personalizada de Docker
├── requirements.txt      # Dependencias necesarias
└── README.md             # Este archivo con documentación del proyecto


```
## A continuación, se explica como probar el servicio con postman

1. Crear una nueva solicitud

Haz clic en “+ New Tab” o en “New” → “HTTP Request”.

Selecciona el método POST.

En el campo de URL escribe:
```
http://localhost:5000/predecir
```
2. Configurar el cuerpo de la solicitud
Ve a la pestaña Body.

Selecciona raw.

En el menú desplegable a la derecha elige JSON.

Escribe el siguiente JSON con los parámetros esperados:
```
{
  "frecuencia_cardiaca": 85,
  "nivel_glucosa": 105,
  "presion_sistolica": 115
}
```

3. Enviar la solicitud
Haz clic en Send.

4. Interpretación de la respuesta
Se podría recibir una respuesta como esta
```
{
  "estado": "ENFERMEDAD LEVE"
}
```

Esto confirma que el contenedor y el servicio están funcionando correctamente.