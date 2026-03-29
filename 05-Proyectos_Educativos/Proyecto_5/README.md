# Proyecto 5: Spaceship Titanic - Competición Interestelar

## 📊 Descripción del Proyecto

Este proyecto se basa en la popular competición de Kaggle **"Spaceship Titanic"**. El objetivo es predecir si un pasajero fue transportado a otra dimensión después de que la nave espacial Titanic chocara con una anomalía espacio-temporal.

### Escenario
Año 2912. Una nave espacial que transportaba emigrantes a exoplanetas recién habitables sufrió un accidente. Casi la mitad de los pasajeros fueron transportados a otra dimensión. Tu misión es ayudar a los equipos de rescate prediciendo quiénes fueron los afectados.

---

## 📁 Estructura del Proyecto

```
Proyecto_5/
├── README.md                                    # Este archivo
├── data/                                        # Conjuntos de datos (train, test)
├── docs/                                        # Documentación detallada
│   ├── competicion.md                           # Resumen de la competición
│   └── diccionario_datos.md                     # Significado de las variables
├── notebooks/                                   # Análisis y Modelado
│   ├── 01_Ingesta_y_EDA.ipynb                   # Exploración de datos
│   └── 02_Feature_Engineering_y_Modelado.ipynb  # Entrenamiento del modelo
├── models/                                      # Modelos entrenados (XGBoost)
├── frontend/                                    # Aplicación Web Interactiva
│   └── app.py                                   # Streamlit App
└── requirements.txt                             # Dependencias del proyecto
```

---

## 🛠️ Tecnologías Utilizadas

- **Análisis de Datos**: Pandas, NumPy.
- **Visualización**: Matplotlib, Seaborn.
- **Machine Learning**: Scikit-learn, XGBoost.
- **Despliegue/Web**: Streamlit.
- **Documentación**: Markdown.

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### 2. Entrenamiento del Modelo
Ejecuta los notebooks en orden dentro de la carpeta `notebooks/`. El segundo cuaderno generará el archivo `models/spaceship_titanic_model.pkl`.

### 3. Aplicación Web
Para lanzar la página web dinámica e interactiva:
```bash
streamlit run frontend/app.py
```

---

## 🔍 Conclusiones Clave

- El uso de **Criogenia** (`CryoSleep`) es el predictor más fuerte para ser transportado.
- La **Cubierta** (`Deck`) y el **Planeta de Origen** (`HomePlanet`) también influyen significativamente en las probabilidades de transporte.
- El modelo **XGBoost** permite alcanzar una precisión cercana al 80% con ingeniería de características básica.
