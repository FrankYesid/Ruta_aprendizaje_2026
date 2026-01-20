# Sistema de Recomendación de Libros o Películas

## Estructura del Proyecto

```
Proyecto_2/
├── data/                       # Archivos de datos para el sistema
│   ├── users.csv               # Usuarios: id, nombre, edad, país (opcional)
│   ├── items.csv               # Ítems: id, título, tipo, géneros, año
│   ├── ratings.csv             # Valoraciones: user_id, item_id, rating, timestamp
│   └── tags.csv                # (Opcional) Etiquetas: user_id, item_id, tag, timestamp
├── notebooks/                  # Cuadernos Jupyter para exploración y modelado
│   ├── 01_exploracion_datos.ipynb
│   ├── 02_preprocesamiento.ipynb
│   ├── 03_modelos_recomendacion.ipynb
│   └── 04_evaluacion_modelos.ipynb
├── src/                        # Código fuente (opcional)
│   ├── pipeline.py
│   └── utils.py
├── LICENSE                     # Licencia del proyecto
└── README.md                   # Documentación del proyecto
```

## Base de Datos

- Usuarios
  - id (int, PK)
  - nombre (string)
  - edad (int, opcional)
  - país (string, opcional)
- Ítems
  - id (int, PK)
  - título (string)
  - tipo (enum: libro|película)
  - géneros (string, lista separada por “|”)
  - año (int)
- Ratings
  - user_id (int, FK usuarios.id)
  - item_id (int, FK ítems.id)
  - rating (float o int, escala 1–5)
  - timestamp (datetime)
- Tags (opcional)
  - user_id (int, FK)
  - item_id (int, FK)
  - tag (string)
  - timestamp (datetime)

Formato recomendado: CSV en la carpeta `data/`. Alternativamente, se puede usar SQLite (`data/recs.db`) con las mismas tablas.

## Requerimientos Detallados

- Software
  - Python 3.9 o superior
  - Jupyter Notebook o JupyterLab
- Librerías
  - pandas, numpy
  - scikit-learn
  - scikit-surprise o implicit/lightfm (según el enfoque)
  - sqlalchemy (si se usa SQLite/PostgreSQL)
  - matplotlib, seaborn
- Instalación
  ```sh
  pip install pandas numpy scikit-learn scikit-surprise sqlalchemy matplotlib seaborn
  ```
  Para modelos basados en factoración:
  ```sh
  pip install implicit lightfm
  ```

## Cómo Visualizar la Información

- Colocar los archivos `users.csv`, `items.csv`, `ratings.csv` en `Proyecto_2/data/`.
- Abrir y ejecutar los cuadernos en `Proyecto_2/notebooks/` para:
  - Explorar estadísticas básicas de usuarios, ítems y ratings.
  - Entrenar modelos de recomendación (filtrado colaborativo, contenido e híbridos).
  - Evaluar con métricas como RMSE, Precision@K, Recall@K y MAP.
- Ejemplo rápido en Python:
  ```python
  import pandas as pd
  users = pd.read_csv("data/users.csv")
  items = pd.read_csv("data/items.csv")
  ratings = pd.read_csv("data/ratings.csv")
  print(users.head(), items.head(), ratings.head(), sep="\n\n")
  ```

## Información Relacionada

- Datasets recomendados:
  - MovieLens (recomendación de películas)
  - Goodreads (recomendación de libros)
- Referencias técnicas:
  - Filtrado colaborativo basado en usuarios y en ítems
  - Factorización de matrices (ALS, SVD)
  - Modelos híbridos combinando contenido y colaborativo

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

