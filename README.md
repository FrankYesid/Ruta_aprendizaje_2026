# Proyectos de Ciencia de Datos: Visualización, Modelado y Análisis

Este repositorio contiene proyectos enfocados en la aplicación de ciencia de datos para resolver problemas en diferentes áreas, desde visualización interactiva hasta integración con el mundo real.

---

## 1. Visualización de Datos
### Objetivo
Explorar y comunicar patrones clave en los datos mediante herramientas de visualización intuitivas e interactivas.

### Proyectos

#### [Proyecto 1: Cambios Climáticos Globales](./01-Visualización_de_Datos/Proyecto_1)
Análisis interactivo de la evolución de las temperaturas terrestres desde el siglo XVIII hasta la actualidad.
- **Técnicas:** Visualización interactiva, Correlación temporal, Mapas de calor.
- **Dataset:** [Global Land Temperatures (Kaggle)](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data).
- **Objetivo:** Visualizar el calentamiento global histórico a nivel de ciudades y países.

#### [Proyecto 2: Análisis de Tráfico Urbano](./01-Visualización_de_Datos/Proyecto_2)
Estudio de patrones de movilidad y densidad de tráfico en entornos urbanos mediante análisis descriptivo.
- **Técnicas:** Análisis de series de tiempo, Mapas de densidad, Histogramas de frecuencia.
- **Dataset:** Datos abiertos de tráfico vehicular.
- **Objetivo:** Identificar horas pico y zonas de alta congestión para optimizar la movilidad.

#### [Proyecto 3: Narrativas COVID en LATAM](./01-Visualización_de_Datos/Proyecto_3)
Construcción de una narrativa visual sobre el impacto y la evolución de la pandemia de COVID-19 en Latinoamérica.
- **Técnicas:** Gráficos de líneas comparativos, Análisis de acumulados, Storytelling con datos.
- **Dataset:** Registros de salud nacionales de países latinoamericanos.
- **Objetivo:** Comparar la evolución de casos y muertes entre diferentes países de la región.

#### [Proyecto 4: Desigualdad de Género](./01-Visualización_de_Datos/Proyecto_4)
Visualización de las brechas sociales y económicas entre géneros en diferentes dimensiones del desarrollo.
- **Técnicas:** Gráficos de barras agrupados, Comparación regional, Análisis de brechas.
- **Dataset:** Encuestas de desarrollo y género de organizaciones internacionales.
- **Objetivo:** Visibilizar las diferencias en ingresos y oportunidades educativas por género.

#### [Proyecto 5: Análisis Ironman](./01-Visualización_de_Datos/Proyecto_5)
Exploración visual del rendimiento y desempeño de atletas en competencias de triatlón de larga distancia.
- **Técnicas:** Distribuciones de frecuencia, Análisis por género y categoría, Boxplots.
- **Dataset:** Resultados oficiales de eventos Ironman.
- **Objetivo:** Analizar los tiempos de ejecución y la demografía de los participantes.

📁 [Ver carpeta completa de Visualización de Datos](./01-Visualización_de_Datos)

## 2. Tratamiento de Datos
### Objetivo
Garantizar que los datos sean confiables y estén listos para análisis y modelado mediante técnicas de preprocesamiento y limpieza.

### Proyectos

#### [Proyecto 1: Preprocesamiento Automatizado](./02-Tratamiento_de_Datos/Proyecto_1)
Desarrollo de flujos de trabajo automatizados para la limpieza y transformación de datos financieros.
- **Técnicas:** Pipelines de Scikit-learn, Imputación de nulos, Escalado de datos.
- **Dataset:** Datos históricos de acciones de Toyota.
- **Objetivo:** Crear un proceso reproducible para preparar datos de series temporales financieras.

#### [Proyecto 2: Calidad del Aire en Colombia](./02-Tratamiento_de_Datos/Proyecto_2)
Limpieza y normalización de datos provenientes de sensores de monitoreo ambiental en diversas regiones.
- **Técnicas:** Análisis geoespacial, Tratamiento de valores atípicos, Normalización.
- **Dataset:** Datos de estaciones de monitoreo ambiental de Colombia.
- **Objetivo:** Estabilizar y limpiar datos de sensores para estudios de salud pública.

#### [Proyecto 3: Extracción de Texto (OCR)](./02-Tratamiento_de_Datos/Proyecto_3)
Transformación de información visual en datos estructurados mediante el reconocimiento óptico de caracteres.
- **Técnicas:** OpenCV, Tesseract OCR, Segmentación de imágenes.
- **Dataset:** Imágenes de documentos y párrafos de texto.
- **Objetivo:** Extraer y organizar texto de imágenes para su posterior análisis textual.

#### [Proyecto 4: Detección de Anomalías ECG](./02-Tratamiento_de_Datos/Proyecto_4)
Procesamiento de señales biomédicas para la identificación de irregularidades en electrocardiogramas.
- **Técnicas:** Procesamiento de señales (SciPy), Transformada de Wavelet, Detección de picos.
- **Dataset:** [MIT-BIH Arrhythmia Database](https://data.mendeley.com/datasets/7dybx7wyfn/3).
- **Objetivo:** Limpiar y segmentar señales de ECG para detectar arritmias cardíacas.

#### [Proyecto 5: Procesamiento de Texto (NLP)](./02-Tratamiento_de_Datos/Proyecto_5)
Preparación de datos textuales de redes sociales para su posterior análisis de sentimiento y engagement.
- **Técnicas:** Tokenización, Lematización, Eliminación de Stopwords.
- **Dataset:** Noticias y publicaciones de agencias como BBC, CNN y Reuters.
- **Objetivo:** Transformar texto no estructurado en representaciones aptas para modelos de lenguaje.

📁 [Ver carpeta completa de Tratamiento de Datos](./02-Tratamiento_de_Datos)

---

## 3. Aplicación de Modelos
### Objetivo
Resolver problemas específicos mediante la implementación de modelos predictivos y de clasificación en diferentes dominios de aplicación.

### Proyectos

#### [Proyecto 1: Predicción de Enfermedades](./03-aplicación_de_modelos/proyecto_1)
Utilización de datos de salud para predecir condiciones médicas como diabetes o enfermedades cardíacas.
- **Técnicas:** Regresión logística, Random Forest, Redes Neuronales.
- **Dataset:** Datos de salud públicos con variables clínicas y de estilo de vida.
- **Objetivo:** Desarrollar un modelo que permita anticipar el riesgo de enfermedades.

#### [Proyecto 2: Optimización de Rutas de Transporte](./03-aplicación_de_modelos/proyecto_2)
Algoritmos para mejorar la logística de distribución de mercancías mediante la resolución del problema de rutas de vehículos (VRP).
- **Técnicas:** OR-Tools (Routing), Algoritmos Genéticos (DEAP), Búsqueda Local.
- **Dataset:** [Vehicle Routing Problem (VRP) de Kaggle](https://www.kaggle.com/datasets/abhilashg23/vehicle-routing-problem-ga-dataset?resource=download).
- **Objetivo:** Encontrar las rutas más eficientes para una flota de vehículos minimizando costos y distancias.

#### [Proyecto 3: Sistemas de Recomendación](./03-aplicación_de_modelos/proyecto_3)
Implementación de motores de recomendación para sugerir contenido relevante basado en el comportamiento histórico del usuario.
- **Técnicas:** Filtrado colaborativo (SVD, KNN), Filtrado basado en contenido (TF-IDF), Modelos Híbridos.
- **Dataset:** [MovieLens Latest Datasets (Small & Full)](https://grouplens.org/datasets/movielens/latest/).
- **Objetivo:** Sugerir películas relevantes a cada usuario según sus preferencias y similitudes con otros usuarios.

#### [Proyecto 4: Predicción del Precio de Vivienda](./03-aplicación_de_modelos/proyecto_4)
Creación de modelos de regresión para estimar el valor comercial de propiedades inmobiliarias basado en múltiples variables.
- **Técnicas:** Regresión Lineal, Gradient Boosting (XGBoost), Random Forest, SVR.
- **Dataset:** [Boston Housing Dataset](file:///d:/GitHub/Ruta_aprendizaje_2024/03-Aplicación_de_Modelos/Proyecto_4/data/BostonHousing.csv).
- **Objetivo:** Proporcionar estimaciones precisas de precios de viviendas para facilitar la toma de decisiones.

#### [Proyecto 5: Clasificación de Residuos](./03-aplicación_de_modelos/proyecto_5)
Implementación de modelos de Deep Learning para la identificación automática de materiales reciclables mediante imágenes.
- **Técnicas:** Redes Neuronales Convolucionales (CNN), Transfer Learning (ResNet18).
- **Dataset:** [Dataset Resized (6 clases)](file:///d:/GitHub/Ruta_aprendizaje_2024/03-Aplicación_de_Modelos/Proyecto_5/data/dataset-resized).
- **Objetivo:** Automatizar la clasificación de residuos (vidrio, papel, cartón, etc.) para mejorar los procesos de reciclaje.

📁 [Ver carpeta completa de Aplicación de Modelos](./03-aplicación_de_modelos)

---

## 4. Análisis Avanzado
### Objetivo
Aplicar técnicas avanzadas de análisis para descubrir patrones, tendencias y predicciones complejas en grandes volúmenes de datos.

### Proyectos

#### [Proyecto 1: Análisis de Engagement en Redes Sociales](./04-Analisis_Avanzado/Proyecto_1)
Análisis exhaustivo del engagement en redes sociales utilizando métricas de interacción (likes, comentarios, compartidos) a través de diversas plataformas y tipos de contenido. Se exploran patrones temporales, el impacto del sentimiento y se desarrolla un modelo predictivo para estimar el éxito de las publicaciones.
- **Técnicas:** EDA Avanzado, Análisis Temporal, Análisis de Sentimiento, Random Forest Regressor, Feature Importance.
- **Dataset:** [Social Media Engagement Dataset (Kaggle)](https://www.kaggle.com/datasets/divyaraj2006/social-media-engagement) - 1000 registros de interacciones en redes sociales.
- **Características clave:** post_id, platform, post_type, likes, comments, shares, sentiment_score.
- **Objetivo:** Identificar tendencias de engagement por plataforma, analizar impacto temporal, evaluar relación entre sentimiento y rendimiento, y predecir el número de likes.

#### [Proyecto 2: Patrones de Consumo Energético](./04-Analisis_Avanzado/Proyecto_2)
Análisis de patrones de consumo eléctrico en un hogar a partir de mediciones tomadas cada minuto durante casi cuatro años. Se explora cómo varía el consumo a lo largo del tiempo, se identifican periodos de mayor demanda y se analizan diferencias entre distintos tipos de uso eléctrico.
- **Técnicas:** Series Temporales Multivariantes, Análisis de Patrones Diarios/Semanales/Estacionales, Detección de Anomalías, Pronóstico.
- **Dataset:** [Individual Household Electric Power Consumption (UCI ML Repository)](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption) - 2,075,259 registros de diciembre 2006 a noviembre 2010.
- **Características clave:** global_active_power, global_reactive_power, voltage, global_intensity, sub_metering_1/2/3.
- **Objetivo:** Visualizar evolución del consumo a distintas escalas temporales, identificar patrones diarios/semanales/estacionales, analizar contribución de submediciones y detectar anomalías.

#### [Proyecto 3: Series Temporales](./04-Analisis_Avanzado/Proyecto_3)
Modelos avanzados para predecir ventas o eventos futuros mediante técnicas de series temporales. Este proyecto se enfoca en ARIMA, Prophet, LSTM y otras metodologías para pronóstico.
- **Técnicas:** ARIMA, Prophet, LSTM, Exponential Smoothing, Análisis de Tendencias.
- **Objetivo:** Desarrollar modelos robusts para predicción de series temporales en contextos financieros, de ventas y eventos futuros.
- **Estructura:** EDA, ARIMA, Prophet, LSTM y comparación de modelos.

#### [Proyecto 4: Análisis de Texto Jurídico](./04-Analisis_Avanzado/Proyecto_4)
Aplicación de NLP avanzado para entender, procesar y clasificar documentos legales. Se realiza extracción de entidades, análisis de relaciones y clasificación automática de textos jurídicos.
- **Técnicas:** Reconocimiento de Entidades Nombradas (NER), Clasificación de Documentos, Extracción de Información, Análisis de Similitud.
- **Herramientas:** SpaCy, NLTK, Modelos de lenguaje.
- **Objetivo:** Automatizar análisis de documentos legales, extraer información clave y clasificar tipos de documentos para agilizar procesos jurídicos.

#### [Proyecto 5: Segmentación de Clientes](./04-Analisis_Avanzado/Proyecto_5)
Agrupamiento de consumidores mediante algoritmos de clustering avanzados (K-means, Clustering Jerárquico, DBSCAN) para identificar segmentos de clientes con características similares.
- **Técnicas:** K-means, Clustering Jerárquico, DBSCAN, Análisis de Validación, Interpretación de Clusters.
- **Objetivo:** Identificar segmentos de clientes homogéneos para estrategias de marketing personalizadas, optimización de recursos y análisis del comportamiento del consumidor.

📁 [Ver carpeta completa de Análisis Avanzado](./04-Analisis_Avanzado)

---

## 5. Proyectos Educativos
# pendiente este segmento
### Objetivo
Desarrollar habilidades prácticas y fomentar el aprendizaje interactivo en ciencia de datos.

### Proyectos
- **[Proyecto 1: Simulación de pandemias](./05-proyectos_educativos/proyecto_1)** - Modelos matemáticos para entender la propagación de enfermedades.
- **[Proyecto 2: Mini bootcamps](./05-proyectos_educativos/proyecto_2)** - Retos semanales para resolver problemas como limpieza de datos.
- **[Proyecto 3: Dashboards educativos](./05-proyectos_educativos/proyecto_3)** - Visualizaciones intuitivas de modelos de ML.
- **[Proyecto 4: Machine Learning explicable (XAI)](./05-proyectos_educativos/proyecto_4)** - Interpretación de modelos complejos.
- **[Proyecto 5: Juegos de datos](./05-proyectos_educativos/proyecto_5)** - Concursos tipo Kaggle con datasets específicos.

📁 [Ver carpeta completa de Proyectos Educativos](./05-proyectos_educativos)

---

## 6. Integración con el Mundo Real
### Objetivo
Implementar soluciones de ciencia de datos en entornos de producción y evaluar su impacto.

### Proyectos
- **[Proyecto 1: Detección de fraude financiero](./06-integracion_con_el_mundo_real/proyecto_1)** - Identificación de actividades sospechosas en transacciones.
- **[Proyecto 2: Pronóstico del clima local](./06-integracion_con_el_mundo_real/proyecto_2)** - Modelos específicos para predicción meteorológica.
- **[Proyecto 3: Análisis de impacto ambiental](./06-integracion_con_el_mundo_real/proyecto_3)** - Evaluación de proyectos usando datos satelitales.
- **[Proyecto 4: Optimización de cultivos](./06-integracion_con_el_mundo_real/proyecto_4)** - Predicción de rendimientos agrícolas según datos climáticos.
- **[Proyecto 5: Monitorización de transporte público](./06-integracion_con_el_mundo_real/proyecto_5)** - Optimización de horarios y rutas mediante análisis de datos.

📁 [Ver carpeta completa de Integración con el Mundo Real](./06-integracion_con_el_mundo_real)

---

## Proceso General

1. **Definición del Problema**: Identificar el problema específico y establecer objetivos claros.
2. **Obtención de Datos**: Recolección de datos relevantes desde fuentes confiables.
3. **Tratamiento de Datos**: Limpieza, transformación y preparación de los datos para el análisis.
4. **Análisis Exploratorio**: Visualización y comprensión inicial de patrones en los datos.
5. **Modelado**: Implementación de modelos predictivos, de clasificación o de agrupamiento según el caso.
6. **Evaluación**: Validación de resultados mediante métricas clave.
7. **Comunicación**: Presentación de los resultados mediante dashboards, reportes o narrativas de datos.

---

## Tecnologías Utilizadas
- **Visualización**: Plotly, Tableau, Matplotlib, Seaborn.
- **Modelado**: Scikit-learn, TensorFlow, PyTorch, OR-Tools, DEAP.
- **Preprocesamiento**: Pandas, NumPy, NLTK, SpaCy.
- **Herramientas**: Jupyter Notebooks, Streamlit, Dash, Power BI.

---

## Licencia

Este repositorio está licenciado bajo **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

