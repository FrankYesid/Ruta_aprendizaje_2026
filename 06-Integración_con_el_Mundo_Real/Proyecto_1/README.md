# Detección de Fraude Financiero

## Descripción

Este proyecto aborda la identificación de actividades sospechosas en transacciones financieras mediante técnicas de análisis exploratorio y modelado supervisado. El objetivo es detectar patrones anómalos que permitan anticipar fraudes y reducir pérdidas económicas.

## Avances realizados

- Se incorporó un conjunto de datos con transacciones financieras y etiquetas de fraude.
- Se creó un notebook de exploración inicial para analizar distribuciones, valores atípicos y posibles señales de riesgo.
- Se desarrolló un script de entrenamiento para entrenar y guardar un modelo de detección.
- Se generó un modelo serializado en [model/fraud_model.joblib](./model/fraud_model.joblib).

## Estructura del proyecto

- [data/](./data): archivos de entrada con transacciones y etiquetas.
- [notebooks/](./notebooks): notebooks de exploración y entrenamiento.
- [train_model_script.py](./train_model_script.py): script reproducible para entrenar el modelo.

## Requerimientos

```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn jupyter
```
