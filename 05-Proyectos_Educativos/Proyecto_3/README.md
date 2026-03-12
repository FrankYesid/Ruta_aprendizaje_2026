# Dashboards Educativos: Visualización de Modelos de ML

## Descripción del Proyecto

Este proyecto educativo se centra en la **interpretación visual de modelos de Machine Learning**. A menudo, los resultados de un modelo se presentan como métricas aisladas (MAE, Accuracy, etc.); sin embargo, para un aprendizaje profundo es vital visualizar cómo se comportan estas predicciones frente a los datos reales.

Utilizando dos dominios clásicos (Precios de Vivienda y Clasificación de Productos), este proyecto enseña a construir visualizaciones intuitivas que facilitan la comunicación de resultados técnicos.

## Datasets

El proyecto utiliza dos conjuntos de datos clave:

1.  **Housing.csv**: 
    - **Contexto:** Precios de viviendas basados en características estructurales (área, habitaciones, etc.).
    - **Uso:** Modelado de **Regresión** y visualización de residuos.
    - **Ubicación:** `data/Housing.csv`
2.  **amazon.csv**: 
    - **Contexto:** Datos de productos de Amazon con ratings y métricas de venta.
    - **Uso:** Modelado de **Clasificación** y visualización de matrices de confusión y curvas ROC.
    - **Ubicación:** `data/amazon.csv`

## Estructura del Proyecto

```
Proyecto_3/
├── data/                  # Conjuntos de datos para entrenamiento
│   ├── Housing.csv        # Dataset de regresión
│   └── amazon.csv         # Dataset de clasificación
├── notebooks/             # Visualizaciones paso a paso
│   ├── 01_visualizacion_regresion.ipynb   # Análisis visual de modelos predictivos
│   └── 02_visualizacion_clasificacion.ipynb # Análisis de métricas de clasificación
├── requirements.txt       # Librerías de visualización y modelado
└── README.md              # Documentación detallada
```

## Requerimientos de Instalación

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

## Objetivos Educativos

1.  **Visualización de Regresión**: Aprender a diagnosticar modelos mediante gráficos de dispersión (Predicho vs Real) y análisis de histogramas de residuos.
2.  **Interpretación de Clasificación**: Ir más allá del Accuracy usando matrices de confusión térmicas y curvas ROC para evaluar la capacidad de discriminación.
3.  **Comunicación de Resultados**: Desarrollar la habilidad de transformar salidas numéricas complejas en narrativas visuales comprensibles para audiencias no técnicas.
4.  **Uso de Herramientas Modernas**: Practicar con `seaborn` y `matplotlib` para crear gráficos profesionales y estéticamente agradables.

---
**Autor:** Frank Yesid
**Año:** 2025
