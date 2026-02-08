# Optimización de Rutas de Transporte (VRP)

## Descripción

Algoritmos para mejorar la logística resolviendo el Vehicle Routing Problem (VRP) y variantes como CVRP (capacidad) y, si aplica, ventanas de tiempo. Se trabaja con el dataset VRP.csv y se implementan enfoques exactos y metaheurísticos.

## Estructura del Proyecto

```
Proyecto_2/
├── data/                       # Datos VRP (VRP.csv) y README.txt
├── notebooks/                  # Flujo completo
│   ├── 01_ingesta_estandarizacion.ipynb
│   ├── 02_eda_visualizacion.ipynb
│   ├── 03_modelo_or_tools.ipynb
│   ├── 04_modelo_ga.ipynb
│   ├── 05_comparacion_resultados.ipynb
│   └── 06_evaluacion_metricas.ipynb
├── src/                        # Código fuente (opcional)
│   ├── loaders.py
│   └── vrp_utils.py
├── LICENSE                     # Licencia del proyecto
└── README.md                   # Documentación del proyecto
```

## Dataset

- Archivo base: `data/VRP.csv`
- Origen: Kaggle – Vehicle Routing Problem GA Dataset: https://www.kaggle.com/datasets/abhilashg23/vehicle-routing-problem-ga-dataset?resource=download
- Estructura esperada:
  - Coordenadas de clientes (X/Y o lat/lon)
  - Demanda por cliente
  - Capacidad de vehículos
  - Índice o coordenadas del depósito
  - (Opcional) Ventanas de tiempo, costos por arco, matriz de distancias

Coloca el archivo `VRP.csv` en la carpeta `data/` y consulta `data/README.txt` para detalles.

## Requerimientos

```bash
pip install pandas numpy matplotlib seaborn scikit-learn ortools networkx deap jupyter
```

## Cómo Trabajar en los Cuadernos

- 01_ingesta_estandarizacion: carga VRP.csv, estandariza tipos y columnas y construye matrices necesarias (distancias, demanda).
- 02_eda_visualizacion: distribuciones de demanda, visualización geográfica de clientes y depósito.
- 03_modelo_or_tools: resolución con OR-Tools (CVRP), obtención de rutas y costo total.
- 04_modelo_ga: metaheurística GA para CVRP/VRP, configuración y resultados.
- 05_comparacion_resultados: comparación entre enfoques (costo, número de vehículos, restricciones).
- 06_evaluacion_metricas: métricas de calidad de ruta, factibilidad y rendimiento.

## Métricas y Resultados

- Costo total de distancia/tiempo
- Cumplimiento de capacidad y ventanas de tiempo (si existen)
- Balanceo entre vehículos
- Visualización de rutas y comparación de enfoques

## Información Relacionada

- Técnicas: OR-Tools (Routing), heurísticas, metaheurísticas (GA), búsqueda local.
- Consideraciones: construcción de matrices de distancia, normalización de coordenadas, tuning de hiperparámetros en GA.
- Fuente de datos: Kaggle – Vehicle Routing Problem GA Dataset.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

