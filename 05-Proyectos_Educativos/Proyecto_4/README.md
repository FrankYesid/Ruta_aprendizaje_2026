# Machine Learning Explicable (XAI)

## Descripción

Este proyecto se centra en la interpretación de modelos de Machine Learning utilizando técnicas de **Explainable AI (XAI)**. A menudo, los modelos potentes como Random Forest actúan como "cajas negras"; aquí aprendemos a abrir esas cajas para entender por qué se toman ciertas decisiones.

## Técnicas y Herramientas

- **SHAP (SHapley Additive exPlanations)**: Basado en la teoría de juegos, proporciona una forma consistente de asignar la contribución de cada característica a la predicción final.
- **LIME (Local Interpretable Model-agnostic Explanations)**: Crea modelos locales aproximados para explicar predicciones individuales.
- **Feature Importance**: Comparación entre la importancia intrínseca del modelo y las técnicas post-hoc (SHAP/LIME).
- **Gráficos de Dependencia**: Visualización del impacto marginal de una característica en la predicción.

## Dataset

- **Boston Housing Dataset**: Datos sobre el valor de las viviendas en Boston, con características como número de habitaciones, tasa de criminalidad, y estatus socioeconómico.

## Estructura del Proyecto

- `01_ingesta_y_eda.ipynb`: Carga de datos y análisis exploratorio inicial.
- `02_modelado_regresion.ipynb`: Entrenamiento de un Random Forest Regressor y evaluación de métricas base.
- `03_explicabilidad_shap.ipynb`: Análisis global y local detallado con SHAP (Summary, Waterfall, Force y Dependence plots).
- `04_explicabilidad_lime.ipynb`: Generación de explicaciones locales con LIME y comparación con SHAP.

## Requerimientos

Instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```
