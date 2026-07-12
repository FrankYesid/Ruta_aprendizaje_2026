# Pronóstico del Clima Local

## Descripción

Este proyecto está enfocado en el desarrollo de modelos de predicción meteorológica a corto plazo utilizando series temporales climáticas. Se han explorado diferentes enfoques, desde análisis descriptivo hasta clasificación y modelos de forecasting con redes LSTM.

## Avances realizados

- Se cargaron y exploraron datasets climáticos de referencia para el entrenamiento de modelos.
- Se realizó feature engineering para preparar las variables de entrada.
- Se implementaron notebooks de clasificación y de pronóstico con LSTM.
- Se generó un reporte inicial en [reports/01_Carga_y_EDA.html](./reports/01_Carga_y_EDA.html).

## Estructura del proyecto

- [data/](./data): archivos de entrenamiento y prueba.
- [notebooks/](./notebooks): notebooks de EDA, ingeniería de variables, clasificación y forecasting.
- [reports/](./reports): entregables iniciales de análisis exploratorio.

## Requerimientos

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels prophet tensorflow jupyter
```
