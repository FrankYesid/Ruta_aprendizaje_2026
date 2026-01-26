# Predicción del Precio de la Vivienda

## Descripción

Modelos que estiman precios de vivienda según ubicación, características y mercado local.

## Estructura Sugerida

```
Proyecto_4/
├── data/                      # Ventas históricas, características de inmuebles
├── notebooks/
│   ├── 01_eda_inmobiliaria.ipynb
│   ├── 02_modelos_regresion.ipynb
│   └── 03_evaluacion_modelos.ipynb
├── src/
│   ├── features.py
│   └── train.py
└── README.md
```

## Requerimientos de Instalación

```bash
pip install pandas numpy scikit-learn xgboost lightgbm matplotlib seaborn jupyter
```

## Uso

- Coloca datos en `data/` con columnas: ubicación, tamaño, habitaciones, año, precio.
- Ejecuta los cuadernos para preparación de datos, entrenamiento y evaluación.

## Información Relacionada

- Técnicas: regresión lineal, árboles de decisión, boosting (XGBoost/LightGBM).
- Métricas: RMSE, MAE, R²; validación cruzada estratificada por zonas.

