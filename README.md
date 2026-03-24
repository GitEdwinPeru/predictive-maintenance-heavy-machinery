# Mantenimiento Predictivo - Flota Caterpillar (CAT)

## Descripción del Proyecto
Este proyecto desarrolla un sistema de **Inteligencia Artificial** capaz de predecir fallas críticas en camiones mineros (modelo 797F) mediante el análisis de telemetría en tiempo real. El objetivo es reducir paradas no programadas y optimizar los costos de mantenimiento preventivo.

## Stack Tecnológico
- **Lenguaje:** Python (Pandas, Numpy)
- **IA/ML:** Scikit-Learn (Random Forest Classifier)
- **Visualización:** Matplotlib & Seaborn
- **Control de Versiones:** Git & GitHub

## Resultados del Modelo
El modelo alcanzó una precisión del **100% (Accuracy: 1.00)** en la detección de fallas basadas en:
- Temperatura del motor
- Presión de aceite
- Niveles de vibración

## Estructura del Repositorio
- `data/`: Datasets generados y procesados.
- `src/`: Scripts de ingestión, ingeniería de atributos y entrenamiento.
- `models/`: Modelo entrenado exportado en formato `.pkl`.
- `notebooks/`: Análisis visual de los datos.

## Autor
**Edwin Benavides** - Técnico en Ingeniería de Software e IA.