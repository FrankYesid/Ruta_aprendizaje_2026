# Proyecto 1: Análisis de Engagement en Redes Sociales

## 📝 Descripción

Este proyecto realiza un análisis exhaustivo del engagement en redes sociales utilizando un dataset que contiene métricas de interacción (likes, comentarios, compartidos) a través de diversas plataformas y tipos de contenido. Se exploran patrones temporales, el impacto del sentimiento y se desarrolla un modelo predictivo para estimar el éxito de las publicaciones.

## 🎯 Objetivos

- **Identificar tendencias de engagement** por plataforma y tipo de contenido.
- **Analizar el impacto temporal** (hora y día) en la interacción del usuario.
- **Evaluar la relación entre el sentimiento** del post y su rendimiento.
- **Desarrollar un modelo de Machine Learning** para predecir el número de likes.
- **Proporcionar recomendaciones estratégicas** basadas en datos para optimizar publicaciones.

## 📊 Dataset

**Fuente**: [Social Media Engagement Dataset (Kaggle)](https://www.kaggle.com/datasets/divyaraj2006/social-media-engagement)
**Archivo**: `data/social_media_engagement1.csv`
**Descripción**: Dataset con 1000 registros de interacciones en redes sociales.

### Características del Dataset:
- **post_id**: Identificador único de la publicación.
- **platform**: Plataforma (Instagram, Facebook, Twitter).
- **post_type**: Tipo de contenido (video, image, text, carousel, poll).
- **post_time**: Marca de tiempo de la publicación.
- **likes**: Número de "me gusta" recibidos (Variable Objetivo).
- **comments**: Número de comentarios.
- **shares**: Número de veces compartido.
- **post_day**: Día de la semana.
- **sentiment_score**: Puntuación de sentimiento (0.0 a 1.0).

## 📂 Estructura del Proyecto

```text
Proyecto_1/
├── data/               # Datasets originales y procesados
│   └── social_media_engagement1.csv
├── notebooks/          # Flujo de trabajo en cuadernos Jupyter
│   ├── 01_ingesta_datos.ipynb
│   ├── 02_eda_engagement.ipynb
│   ├── 03_preprocesamiento_fechas.ipynb
│   ├── 04_analisis_sentimiento_engagement.ipynb
│   ├── 05_modelado_prediccion_likes.ipynb
│   └── 06_conclusiones_dashboard.ipynb
├── src/                # Módulos de código fuente (Python)
│   ├── __init__.py
│   ├── data_loader.py
│   ├── feature_engineering.py
│   └── visualization.py
├── docs/               # Documentación técnica
├── models/             # Modelos entrenados y serializados
├── requirements.txt    # Dependencias del proyecto
├── LICENSE             # Licencia MIT
└── README.md           # Documentación general
```

## � Flujo de Trabajo

### 1. Ingesta de Datos
- Carga del dataset mediante módulos personalizados en `src/`.
- Validación de tipos de datos y detección de valores nulos.
- Resumen inicial de la estructura del dataset.

### 2. Análisis Exploratorio (EDA)
- Distribución de posts por plataforma y tipo.
- Análisis de correlación entre likes, comentarios y compartidos.
- Visualización de métricas promedio por categoría.

### 3. Preprocesamiento y Análisis Temporal
- Conversión de `post_time` a objetos datetime.
- Extracción de características: Hora del día, Mes, Día de la semana.
- Análisis de "horas pico" de interacción.

### 4. Análisis de Sentimiento
- Estudio de la correlación entre `sentiment_score` y engagement.
- Comparativa de rendimiento de posts positivos vs. neutros por plataforma.
- Identificación de sesgos de plataforma respecto al tono del contenido.

### 5. Modelado Predictivo
- Preparación de datos (One-Hot Encoding para variables categóricas).
- Entrenamiento de un **Random Forest Regressor**.
- Evaluación mediante **R2 Score** y **RMSE**.
- Análisis de importancia de características (Feature Importance).

### 6. Conclusiones e Insights
- Resumen de los hallazgos más críticos.
- Visualización final de resultados (Dashboard-style).
- Recomendaciones para la toma de decisiones estratégicas en marketing digital.

## 🛠️ Instalación y Uso

1. **Clonar el repositorio** y navegar a la carpeta del proyecto.
2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar los notebooks**: Abrir Jupyter Lab/Notebook y ejecutar los archivos en la carpeta `notebooks/` en orden correlativo (01 al 06).

## ⚖️ Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulte el archivo [LICENSE](file:///d:/GitHub/Ruta_aprendizaje_2024/04-Analisis_Avanzado/Proyecto_1/LICENSE) para más información.
