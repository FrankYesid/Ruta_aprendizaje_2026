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
Análisis preventivo utilizando datos clínicos para predecir condiciones médicas como diabetes o enfermedades cardiovasculares mediante modelos de clasificación.
- **Técnicas:** Regresión logística, Random Forest, Redes Neuronales, Análisis de importancia.
- **Dataset:** [CVD Cleaned (Kaggle)](file:///d:/GitHub/Ruta_aprendizaje_2024/03-aplicación_de_modelos/proyecto_1/data/CVD_cleaned.csv) - Datos de salud con variables clínicas y estilo de vida.
- **Objetivo:** Desarrollar un modelo robusto que permita anticipar el riesgo de enfermedades crónicas basándose en perfiles de pacientes.

#### [Proyecto 2: Optimización de Rutas de Transporte](./03-aplicación_de_modelos/proyecto_2)
Resolución del problema de rutas de vehículos (VRP) para mejorar la logística de distribución mediante algoritmos de optimización y búsqueda heurística.
- **Técnicas:** OR-Tools (Routing), Algoritmos Genéticos (DEAP), Búsqueda Local, Metaheurísticas.
- **Dataset:** [Vehicle Routing Problem (VRP) de Kaggle](file:///d:/GitHub/Ruta_aprendizaje_2024/03-aplicación_de_modelos/proyecto_2/data/VRP.csv).
- **Objetivo:** Encontrar las rutas más eficientes para una flota de vehículos minimizando costos operativos y distancias recorridas.

#### [Proyecto 3: Sistemas de Recomendación](./03-aplicación_de_modelos/proyecto_3)
Implementación de motores de recomendación para sugerir contenido personalizado basado en el comportamiento histórico del usuario y similitud de ítems.
- **Técnicas:** Filtrado colaborativo (SVD, KNN), Filtrado basado en contenido (TF-IDF), Modelos Híbridos.
- **Dataset:** [MovieLens Latest Datasets (Small & Full)](https://grouplens.org/datasets/movielens/latest/).
- **Objetivo:** Sugerir películas relevantes a cada usuario según sus preferencias históricas y patrones de consumo de otros usuarios similares.

#### [Proyecto 4: Predicción del Precio de Vivienda](./03-aplicación_de_modelos/proyecto_4)
Creación de modelos de regresión avanzados para estimar el valor comercial de propiedades inmobiliarias basado en múltiples variables socioeconómicas y geográficas.
- **Técnicas:** Regresión Lineal, Gradient Boosting (XGBoost), Random Forest, SVR, Feature Engineering.
- **Dataset:** [Boston Housing Dataset](file:///d:/GitHub/Ruta_aprendizaje_2024/03-aplicación_de_modelos/proyecto_4/data/BostonHousing.csv).
- **Objetivo:** Proporcionar estimaciones precisas de precios de viviendas para facilitar la toma de decisiones en el sector inmobiliario.

#### [Proyecto 5: Clasificación de Residuos](./03-aplicación_de_modelos/proyecto_5)
Implementación de modelos de Deep Learning para la identificación automática de materiales reciclables mediante visión artificial.
- **Técnicas:** Redes Neuronales Convolucionales (CNN), Transfer Learning (ResNet18), PyTorch.
- **Dataset:** [Dataset Resized (6 clases)](file:///d:/GitHub/Ruta_aprendizaje_2024/03-aplicación_de_modelos/proyecto_5/data/dataset-resized).
- **Objetivo:** Automatizar la clasificación de residuos (vidrio, papel, cartón, etc.) para optimizar los procesos de reciclaje y gestión ambiental.

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

#### [Proyecto 3: Series Temporales Financieras](./04-Analisis_Avanzado/Proyecto_3)
Pronóstico de precios de activos financieros utilizando series de tiempo multivariantes con retardos (lags) de múltiples acciones tecnológicas y bancarias (AAPL, GOOGL, MSFT, AMZN, JPM).
- **Técnicas:** Análisis de Retardos (Lags t-0 a t-29), ARIMA, ydata-profiling, Análisis de Retornos Logarítmicos.
- **Dataset:** [Financial Time Series Dataset (Kaggle)](https://www.kaggle.com/datasets/programmer3/financial-time-series-dataset) - Datos históricos con 30 retardos para predicción del target.
- **Características clave:** AAPL, GOOGL, MSFT, AMZN, JPM (lags t-0 a t-29), target.
- **Objetivo:** Desarrollar modelos robustos de forecasting para predecir el comportamiento futuro de activos financieros basados en dependencias temporales.

#### [Proyecto 4: Análisis de Texto Jurídico (EUR-Lex)](./04-Analisis_Avanzado/Proyecto_4)
Aplicación de NLP avanzado para entender, procesar y extraer información de documentos legales a gran escala utilizando el corpus de la Unión Europea.
- **Técnicas:** NER (Reconocimiento de Entidades), Clasificación de Texto, Modelado de Tópicos (LDA), Búsqueda Semántica con Embeddings.
- **Dataset:** [EurlexResources (Hugging Face)](https://huggingface.co/datasets/joelniklaus/eurlex_resources) - Corpus masivo de jurisprudencia y directivas de la UE.
- **Objetivo:** Automatizar el análisis de documentos legales, extraer entidades clave (personas, organizaciones) y permitir búsquedas semánticas eficientes.

#### [Proyecto 5: Segmentación de Clientes](./04-Analisis_Avanzado/Proyecto_5)
Agrupamiento de consumidores mediante algoritmos de clustering avanzado para identificar segmentos de mercado mayoristas con comportamientos de compra similares.
- **Técnicas:** K-means, Clustering Jerárquico, DBSCAN, Análisis de Silueta, PCA, Estandarización de datos.
- **Dataset:** [Wholesale Customers Dataset (UCI)](file:///d:/GitHub/Ruta_aprendizaje_2024/04-Analisis_Avanzado/Proyecto_5/data/Wholesale%20customers%20data.csv) - 440 registros de clientes mayoristas.
- **Objetivo:** Identificar grupos de clientes homogéneos para optimizar la cadena de suministro y diseñar estrategias de marketing personalizadas.

📁 [Ver carpeta completa de Análisis Avanzado](./04-Analisis_Avanzado)

---

## 5. Proyectos Educativos
### Objetivo
Desarrollar habilidades prácticas y fomentar el aprendizaje interactivo en ciencia de datos a través de retos y simulaciones guiadas.

### Proyectos

#### [Proyecto 1: Simulación de Pandemias (Modelo SIR)](./05-proyectos_educativos/proyecto_1)
Estudio de la dinámica de propagación de enfermedades infecciosas utilizando modelos matemáticos aplicados a datos reales de COVID-19.
- **Técnicas:** Modelo SIR, Ecuaciones Diferenciales (odeint), Optimización de Parámetros (minimize), Análisis de Series Temporales.
- **Dataset:** [Johns Hopkins COVID-19 Data (GitHub)](https://github.com/CSSEGISandData/COVID-19) - Series mundiales diarias (2020-2023).
- **Objetivo:** Simular brotes epidémicos y ajustar parámetros teóricos ($\beta$, $\gamma$, $R_0$) a picos de contagio reales.

#### [Proyecto 2: Retos de Limpieza de Datos](./05-proyectos_educativos/proyecto_2)
Mini bootcamp enfocado en el diagnóstico y corrección de problemas de calidad en datasets "sucios" del mundo real.
- **Técnicas:** Expresiones Regulares (Regex), Normalización de formatos, Tratamiento de Nulos, Visualización de Calidad.
- **Dataset:** [Dirty Dataset for Data Cleaning (Kaggle)](file:///d:/GitHub/Ruta_aprendizaje_2024/05-proyectos_educativos/proyecto_2/data/my_file%20(1).csv) - Giras musicales con múltiples inconsistencias.
- **Objetivo:** Transformar datos ruidosos en un dataset estructurado y confiable para el análisis estadístico.

#### [Proyecto 3: Visualización de Modelos de ML](./05-proyectos_educativos/proyecto_3)
Interpretación intuitiva de resultados de Machine Learning mediante técnicas de visualización diagnóstica para modelos de regresión y clasificación.
- **Técnicas:** Análisis de Residuos, Matrices de Confusión térmicas, Curvas ROC/AUC, Gráficos de dispersión Predicho vs Real.
- **Dataset:** [Housing Prices](file:///d:/GitHub/Ruta_aprendizaje_2024/05-proyectos_educativos/proyecto_3/data/Housing.csv) y [Amazon Products](file:///d:/GitHub/Ruta_aprendizaje_2024/05-proyectos_educativos/proyecto_3/data/amazon.csv).
- **Objetivo:** Comunicar el rendimiento y los errores de los modelos de forma clara para facilitar la toma de decisiones técnicas.

#### [Proyecto 4: Machine Learning explicable (XAI)](./05-proyectos_educativos/proyecto_4)
Interpretación de modelos de "caja negra" mediante técnicas que permiten explicar el porqué de las predicciones individuales y globales.
- **Técnicas:** SHAP (Waterfall, Force, Summary plots), LIME, Feature Importance, Gráficos de dependencia.
- **Dataset:** [Boston Housing Dataset](file:///d:/GitHub/Ruta_aprendizaje_2024/05-proyectos_educativos/proyecto_4/data/BostonHousing.csv).
- **Objetivo:** Abrir la "caja negra" de modelos complejos para garantizar transparencia, ética y confianza en las predicciones.

#### [Proyecto 5: Spaceship Titanic - Competición de Kaggle](./05-proyectos_educativos/proyecto_5)
Resolución de una competición de clasificación binaria para predecir el transporte de pasajeros a otra dimensión mediante modelos avanzados.
- **Técnicas:** XGBoost, Imputación de nulos, Ingeniería de características (Cabin split), Despliegue con Streamlit.
- **Dataset:** [Spaceship Titanic (Kaggle)](file:///d:/GitHub/Ruta_aprendizaje_2024/05-proyectos_educativos/proyecto_5/data/train.csv).
- **Objetivo:** Alcanzar una alta precisión en la predicción de supervivencia interestelar y desplegar una aplicación web interactiva para visualizar el modelo.

📁 [Ver carpeta completa de Proyectos Educativos](./05-proyectos_educativos)

---

## 6. Integración con el Mundo Real
### Objetivo
Implementar soluciones de ciencia de datos en entornos de producción y evaluar su impacto social y económico.

### Proyectos

#### [Proyecto 1: Detección de Fraude Financiero](./06-Integración_con_el_Mundo_Real/Proyecto_1)
Aplicación inicial de análisis de datos y modelado para identificar actividades sospechosas en transacciones financieras.
- **Técnicas:** Exploración de datos, modelado supervisado y entrenamiento reproducible.
- **Avance actual:** se cuenta con datos, notebooks de EDA y entrenamiento, además de un script para entrenar un modelo guardado en [06-Integración_con_el_Mundo_Real/Proyecto_1/model/fraud_model.joblib](./06-Integración_con_el_Mundo_Real/Proyecto_1/model/fraud_model.joblib).
- **Objetivo:** fortalecer la detección temprana de fraudes y mejorar la capacidad de clasificación.

#### [Proyecto 2: Pronóstico del Clima Local](./06-Integración_con_el_Mundo_Real/Proyecto_2)
Desarrollo de modelos meteorológicos para predicciones a corto plazo y análisis de series temporales climáticas.
- **Técnicas:** EDA, feature engineering, clasificación y forecasting con LSTM.
- **Avance actual:** se han desarrollado notebooks para carga, análisis exploratorio, ingeniería de variables y pronóstico.
- **Objetivo:** construir modelos útiles para alertas tempranas y toma de decisiones en contextos locales.

#### [Proyecto 3: Análisis de Impacto Ambiental](./06-Integración_con_el_Mundo_Real/Proyecto_3)
Análisis de datos ambientales con enfoque en calidad del aire y su relación con la salud pública.
- **Técnicas:** exploración, preprocesamiento y modelado con interpretabilidad mediante SHAP.
- **Fuente:** [WHO Air Quality Database](https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database).
- **Avance actual:** se tienen notebooks de exploración, preprocesamiento y modelado con hiperparámetros.
- **Objetivo:** extraer insights útiles sobre la calidad del aire y sus factores asociados.

#### [Proyecto 4: Optimización de Cultivos](./06-Integración_con_el_Mundo_Real/Proyecto_4)
Propuesta para predecir rendimientos agrícolas y apoyar decisiones de manejo en entornos productivos.
- **Técnicas:** análisis de datos agrícolas, modelado predictivo y evaluación de variables climáticas y del suelo.
- **Avance actual:** se estableció la estructura base del proyecto con carpeta para datos y análisis.
- **Objetivo:** mejorar la productividad agrícola mediante decisiones más informadas.

#### [Proyecto 5: Monitorización de Transporte Público](./06-Integración_con_el_Mundo_Real/Proyecto_5)
Análisis de movilidad urbana para optimizar rutas, horarios y operación de sistemas de transporte.
- **Técnicas:** análisis exploratorio de datos, visualización y propuestas de optimización.
- **Avance actual:** se organizó la estructura inicial del proyecto para trabajos posteriores de EDA y modelado.
- **Objetivo:** mejorar la eficiencia del transporte y la experiencia de los usuarios.

📁 [Ver carpeta completa de Integración con el Mundo Real](./06-Integración_con_el_Mundo_Real)

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
- **Visualización**: Plotly, Matplotlib, Seaborn.
- **Modelado**: Scikit-learn, TensorFlow, PyTorch, OR-Tools, DEAP.
- **Preprocesamiento**: Pandas, NumPy, NLTK, SpaCy.
- **Herramientas**: Jupyter Notebooks, Streamlit y Dash.

---

## Licencia

Este repositorio está licenciado bajo **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

