# Proyecto 4: Predicción del Precio de Vivienda

## Descripción

Este proyecto implementa modelos de machine learning para predecir precios de viviendas en Boston utilizando el famoso dataset Boston Housing. Se exploran múltiples técnicas de regresión para encontrar el mejor modelo predictivo.

## Objetivos

- Desarrollar modelos precisos para predecir precios de viviendas
- Comparar diferentes algoritmos de regresión
- Implementar ingeniería de características
- Evaluar modelos con métricas apropiadas
- Crear un pipeline completo de ML

## Dataset

**Fuente**: Boston Housing Dataset
**Archivo**: `data/BostonHousing.csv`
**Descripción**: Dataset clásico con 506 registros y 14 características de viviendas en Boston

### Características del Dataset:
- **CRIM**: Tasa de criminalidad per cápita por ciudad
- **ZN**: Proporción de terrenos residenciales zonificados para lotes de más de 25,000 pies cuadrados
- **INDUS**: Proporción de acres de negocios no minoristas por ciudad
- **CHAS**: Variable ficticia de Charles River (1 si el tracto limita con el río; 0 en caso contrario)
- **NOX**: Concentración de óxidos nítricos (partes por 10 millones)
- **RM**: Número promedio de habitaciones por vivienda
- **AGE**: Proporción de unidades ocupadas por sus propietarios construidas antes de 1940
- **DIS**: Distancias ponderadas a cinco centros de empleo de Boston
- **RAD**: Índice de accesibilidad a carreteras radiales
- **TAX**: Tasa de impuesto a la propiedad de valor completo por $10,000
- **PTRATIO**: Proporción alumno-maestro por ciudad
- **B**: 1000(Bk - 0.63)^2 donde Bk es la proporción de negros por ciudad
- **LSTAT**: % de población de clase baja
- **MEDV**: Valor medio de viviendas ocupadas por sus propietarios en $1000 (variable objetivo)

## Estructura del Proyecto

```
proyecto_4/
├── data/
│   ├── BostonHousing.csv          # Dataset original
│   ├── README.txt                 # Información del dataset
│   └── processed/                 # Datos procesados
├── notebooks/
│   ├── 01_ingesta_estandarizacion.ipynb
│   ├── 02_eda_visualizacion.ipynb
│   ├── 03_preparacion_datos.ipynb
│   ├── 04_modelos_regresion.ipynb
│   ├── 05_modelos_avanzados.ipynb
│   └── 06_evaluacion_metricas.ipynb
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── model_evaluation.py
├── models/                        # Modelos entrenados
├── reports/                       # Reportes y visualizaciones
└── requirements.txt
```

## Flujo de Trabajo

### 1. Ingesta y Estandarización
- Carga del dataset Boston Housing
- Validación de datos faltantes
- Estandarización de formatos
- División inicial de datos

### 2. Análisis Exploratorio (EDA)
- Estadísticas descriptivas
- Análisis de distribuciones
- Detección de valores atípicos
- Matriz de correlaciones
- Visualizaciones interactivas

### 3. Preparación de Datos
- Limpieza de datos
- Ingeniería de características
- Escalado de variables
- Codificación de variables categóricas
- Selección de características

### 4. Modelos de Regresión
- **Regresión Lineal**: Modelo base
- **Regresión Ridge**: Regularización L2
- **Regresión Lasso**: Regularización L1
- **Elastic Net**: Combinación de regularizaciones

### 5. Modelos Avanzados
- **Random Forest**: Ensamble de árboles
- **Gradient Boosting**: XGBoost
- **Support Vector Regression**: SVR
- **k-Nearest Neighbors**: KNN Regressor

### 6. Evaluación y Métricas
- **MSE (Mean Squared Error)**: Error cuadrático medio
- **RMSE (Root Mean Squared Error)**: Raíz del error cuadrático medio
- **MAE (Mean Absolute Error)**: Error absoluto medio
- **R² Score**: Coeficiente de determinación
- **Cross-Validation**: Validación cruzada
- **Análisis de residuos**

## Modelos Implementados

### Modelos Lineales
- Linear Regression
- Ridge Regression
- Lasso Regression
- Elastic Net

### Modelos No Lineales
- Random Forest Regressor
- Gradient Boosting (XGBoost)
- Support Vector Regression
- k-Nearest Neighbors

## Resultados Esperados

- Comparación detallada de modelos
- Identificación del mejor modelo predictivo
- Análisis de importancia de características
- Visualizaciones de predicciones vs valores reales
- Recomendaciones para producción

## Requisitos de Instalación

Ver archivo `requirements.txt` para las dependencias específicas del proyecto.

## Uso

1. Ejecutar los notebooks en orden numérico
2. Cada notebook genera outputs y visualizaciones
3. Los modelos entrenados se guardan en `models/`
4. Los reportes se generan en `reports/`

## Notas

- El dataset Boston Housing es un dataset clásico ampliamente utilizado en educación
- Se recomienda explorar la ingeniería de características avanzada
- Los modelos pueden ser mejorados con tuning de hiperparámetros
- Considerar técnicas de ensemble para mejorar predicciones

## Referencias

- Harrison, D. and Rubinfeld, D.L. (1978) Hedonic prices and the demand for clean air
- UCI Machine Learning Repository: Boston Housing Dataset
- Scikit-learn documentation for regression models