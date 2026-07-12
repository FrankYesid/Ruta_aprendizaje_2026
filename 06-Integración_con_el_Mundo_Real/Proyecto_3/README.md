# Análisis de Impacto Ambiental

## Descripción

Este proyecto está orientado al análisis de datos ambientales con énfasis en calidad del aire y variables asociadas al impacto sobre la salud pública. La propuesta se apoya en una fuente oficial de la OMS para trabajar con datos de calidad del aire.

## Fuente de datos

- [WHO Air Quality Database](https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database)

## Avances realizados

- Se elaboró una primera exploración de los datos para identificar patrones, valores faltantes y variables relevantes.
- Se realizó un proceso de preprocesamiento para preparar los datos para modelado.
- Se desarrolló un notebook de modelado que incluye ajustes de hiperparámetros y análisis con SHAP.

## Estructura del proyecto

- [data/](./data): datos del proyecto.
- [notebook/](./notebook): notebooks de exploración, preprocesamiento y modelado.

## Requerimientos

```bash
pip install pandas numpy geopandas rasterio shapely matplotlib seaborn scikit-learn xgboost shap jupyter
```
