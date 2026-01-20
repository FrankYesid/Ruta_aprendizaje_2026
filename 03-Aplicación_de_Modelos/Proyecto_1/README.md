# Predicción de Riesgo de Enfermedades Cardiovasculares Basado en Factores de Estilo de Vida

## Sobre el Conjunto de Datos

El **conjunto de datos de predicción de enfermedades cardiovasculares (CVDs)** utiliza factores de estilo de vida personales para predecir riesgos potenciales para la salud. El dataset proviene del **Behavioral Risk Factor Surveillance System (BRFSS)**, un sistema integral de encuestas telefónicas en los Estados Unidos que recopila datos sobre comportamientos de salud, enfermedades crónicas y uso de servicios preventivos.

### Preprocesamiento del Conjunto de Datos BRFSS

El conjunto de datos original de BRFSS contenía **304 variables únicas**. De este extenso dataset, se seleccionaron **19 variables** relacionadas con los factores de estilo de vida que contribuyen significativamente a la evaluación del riesgo de enfermedades cardiovasculares.

- [Consulta mi cuaderno aquí](#)
- [Accede a la aplicación web que creé aquí](#)
- [Lee el artículo de investigación basado en este dataset](#)

## Estructura del Proyecto

```
Proyecto_1/
├── notebooks/            # Cuadernos Jupyter para análisis de datos y entrenamiento de modelos
│   ├── 01_preanalisis.ipynb
│   ├── 02_preprocesamiento.ipynb
│   ├── 03_analisis_descriptivo.ipynb
│   ├── 04_desarrollo_modelos.ipynb
│   ├── 05_validacion_modelos.ipynb
├── data/                # Contiene el conjunto de datos utilizado en este estudio
│   ├── brfss_cvd_risk.csv
├── README.md            # Documentación del proyecto
```

## Contenido del Proyecto

### 1. Preanálisis del Conjunto de Datos

1.1 Carga de la librería de Pandas y del dataset\
1.2 Número de variables y observaciones del dataset\
1.3 Nombre de las variables\
1.4 Características generales de las variables\
1.5 Visualización de las primeras filas del dataset\
1.6 Descripción estadística general del dataset\
1.7 Correlación entre las variables numéricas

### 2. Preparación y Transformación de los Datos

2.1 Comprobación de la existencia de valores faltantes\
2.2 Identificación de valores atípicos (outliers)\
2.3 Creación de una columna con el total de enfermedades\
2.4 Creación de una columna con el estado de peso en función del IMC (BMI)\
2.5 Reordenación de las columnas\
2.6 Cambio de tipos de datos\
2.7 Normalización de ciertas variables

### 3. Análisis Descriptivo del Conjunto de Datos

3.1 Número de hombres y mujeres en el conjunto de datos\
3.2 Número de personas que padecen distintas patologías\
3.3 Patologías por sexo\
3.4 Matriz de correlación entre variables\
3.5 Análisis de tendencia de fumadores y casos de cáncer en diferentes rangos de edad\
3.6 Relación entre el peso y la depresión\
3.7 Consumo de alimentos por grupos de edad\
3.8 Enfermedades a lo largo de los años\
3.9 Consideración del paciente sobre su salud comparada con el número de enfermedades que padece\
3.10 Consumo de alcohol por grupo de edad\
3.11 Enfermedades del corazón en relación con el consumo de frutas y verduras

### 4. Desarrollo de Modelos de Predicción

4.1 Regresión Logística\
4.2 Random Forest\
4.3 Máquinas de Soporte Vectorial (SVM)\
4.4 Redes Neuronales

### 5. Validación de Modelos de Predicción

5.1 Validación del modelo de Redes Neuronales aplicado a 'Heart\_Disease'\
5.2 Validación del modelo de Redes Neuronales aplicado a 'Diabetes'\
5.3 Validación del modelo de Random Forest aplicado a 'Skin\_Cancer'\
5.4 Validación del modelo de Random Forest aplicado a 'Other\_Cancer'\
5.5 Validación del modelo de Redes Neuronales aplicado a 'Depression'\
5.6 Validación del modelo de Redes Neuronales aplicado a 'Arthritis'

## Cómo Usar Este Repositorio

1. Clona el repositorio:
   ```sh
   git clone https://github.com/yourusername/.git
   ```
2. Instala las dependencias:
   ```sh
   pip install pandas numpy scikit-learn matplotlib seaborn jupyter tensorflow
   ```
3. Ejecuta los cuadernos Jupyter en la carpeta `notebooks/` para explorar el conjunto de datos y entrenar los modelos.


