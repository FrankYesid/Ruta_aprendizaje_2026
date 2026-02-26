# Series Temporales Financieras

## Descripción del Proyecto

Este proyecto explora y modela series temporales financieras utilizando un dataset multivariante con retardos (lags) de activos tecnológicos y bancarios. Se analiza el comportamiento de acciones como **Apple (AAPL)**, **Google (GOOGL)**, **Microsoft (MSFT)**, **Amazon (AMZN)** y **JPMorgan (JPM)**, con una ventana de observación de 30 días (t-0 a t-29) para predecir un valor objetivo (target).

El objetivo es entender la dinámica temporal de los activos, realizar un análisis exploratorio detallado y construir modelos de pronóstico (Forecasting) que aprovechen la información histórica de los retardos.

## Dataset

- **Nombre:** Financial Time Series Dataset
- **Fuente:** Kaggle
- **URL oficial del dataset:** [https://www.kaggle.com/datasets/programmer3/financial-time-series-dataset](https://www.kaggle.com/datasets/programmer3/financial-time-series-dataset)
- **Estructura de Columnas:** Incluye 30 retardos por cada activo financiero (AAPL_t-0, GOOGL_t-0... JPM_t-29) y una columna `target`.

El archivo de trabajo principal se encuentra en:

- `data/financial_timeseries_dataset.csv`

## Estructura del Proyecto

```
Proyecto_3/
├── data/
│   └── financial_timeseries_dataset.csv
├── notebooks/
│   ├── 01_ingesta_y_profile.ipynb         # Carga del CSV y perfilado automático con ydata-profiling
│   ├── 02_eda_serie_temporal.ipynb        # Análisis exploratorio de la serie temporal y retornos
│   └── 03_modelado_arima.ipynb            # Modelo ARIMA para pronóstico de precios
├── requirements.txt
└── README.md
```

## Requerimientos de Instalación

Instala las dependencias principales con:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels ydata-profiling jupyter
```

O desde la carpeta del proyecto:

```bash
pip install -r requirements.txt
```

## Flujo de Trabajo

1. **01_ingesta_y_profile.ipynb**  
   Carga el archivo `financial_timeseries_dataset.csv`, revisa la estructura básica del dataset y genera un informe detallado con `ydata-profiling` (`financial_timeseries_profile.html`).

2. **02_eda_serie_temporal.ipynb**  
   Convierte la columna de fecha a un índice temporal, selecciona una serie de precios (por ejemplo, `Close`), analiza su evolución, calcula retornos logarítmicos y estudia la correlación entre variables numéricas.

3. **03_modelado_arima.ipynb**  
   Prepara una serie de precios univariada, la divide en conjuntos de entrenamiento y prueba respetando el orden temporal, entrena un modelo ARIMA básico y evalúa su desempeño mediante métricas como MAE y RMSE, además de una comparación visual entre valores reales y pronosticados.
