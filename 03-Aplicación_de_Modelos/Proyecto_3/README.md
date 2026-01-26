# Optimización de Rutas de Transporte

## Descripción

Proyecto para optimizar rutas logísticas y reducir tiempos/costos de entrega usando algoritmos de optimización y aprendizaje automático.

## Estructura Sugerida

```
Proyecto_3/
├── data/                      # Datos de tráfico, GPS y entregas
├── notebooks/                 # Cuadernos para EDA y modelado
│   ├── 01_eda_datos.ipynb
│   ├── 02_modelado_rutas.ipynb
│   └── 03_evaluacion.ipynb
├── src/                       # Código fuente
│   ├── optimizer.py
│   └── utils.py
└── README.md
```

## Requerimientos de Instalación

```bash
pip install pandas numpy matplotlib seaborn scikit-learn ortools networkx jupyter
```

## Uso

- Coloca los datos en `data/` con columnas: ubicaciones, tiempos, costos, restricciones.
- Ejecuta los cuadernos en `notebooks/` para explorar, optimizar y evaluar rutas.

## Información Relacionada

- Técnicas: algoritmos de optimización (TSP/VRP), RNN para estimación de tiempos, aprendizaje por refuerzo.
- Fuentes de datos: registros GPS, tiempos históricos de entrega, datos de tráfico.

