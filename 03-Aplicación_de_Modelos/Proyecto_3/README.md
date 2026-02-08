# Sistema de Recomendación con MovieLens

## Descripción

Proyecto de recomendación de películas utilizando los datasets de MovieLens. Incluye ingesta y estandarización de datos, análisis exploratorio y visualización, y entrenamiento de modelos de recomendación (colaborativo, contenido e híbrido).

## Estructura Sugerida

```
Proyecto_3/
├── data/                      # MovieLens (ml-latest-small / ml-latest) y README.txt
├── notebooks/                 # Cuadernos para el flujo completo
│   ├── 01_ingesta_estandarizacion.ipynb
│   ├── 02_eda_visualizacion.ipynb
│   ├── 03_modelos_filtrado_colaborativo.ipynb
│   ├── 04_modelos_contenido.ipynb
│   ├── 05_modelo_hibrido.ipynb
│   └── 06_evaluacion_metricas.ipynb
├── src/                       # Código fuente
│   ├── loaders/
│   │   └── movielens.py
│   ├── models/
│   │   ├── collaborative.py
│   │   ├── content.py
│   │   └── hybrid.py
│   └── utils.py
└── README.md
```

## Datasets

- MovieLens Small (ml-latest-small): 100.000 ratings y ~3.600 tags en ~9.000 películas por ~600 usuarios.
- MovieLens Full (ml-latest): ~33M ratings y ~2M tags en ~86.000 películas por ~330.975 usuarios; incluye tag genome con ~14M relevancias en ~1.100 tags.
- Descarga: https://grouplens.org/datasets/movielens/latest/

Coloca el contenido descomprimido en `Proyecto_3/data/`:
- ml-latest-small/
  - ratings.csv, movies.csv, tags.csv, links.csv
- ml-latest/ (opcional si trabajas con el dataset completo)
  - ratings.csv, movies.csv, tags.csv, links.csv, genome-scores.csv, genome-tags.csv

## Requerimientos de Instalación

```bash
pip install pandas numpy scikit-learn scikit-surprise implicit lightfm sqlalchemy matplotlib seaborn jupyter
```

## Uso

- Coloca los datasets en `data/` (ver sección Datasets) y revisa `data/README.txt`.
- Ejecuta los cuadernos en `notebooks/` para:
  - Ingesta, estandarización y unión de ratings, movies, tags y links.
  - EDA y visualización de distribución de ratings, usuarios y películas.
  - Entrenamiento de modelos:
    - Filtrado colaborativo (User/Item-KNN, SVD en Surprise, ALS en implicit).
    - Basado en contenido (TF-IDF/BOW sobre géneros y tags).
    - Enfoque híbrido combinando señales de colaborativo y contenido.
  - Evaluación con RMSE (predicción), y ranking: Precision@K, Recall@K, MAP, NDCG.

## Información Relacionada

- Técnicas: filtrado colaborativo (vecindarios, factoración), contenido (TF-IDF, Word2Vec opcional), híbridos.
- Consideraciones: sesgo de popularidad, cold-start (nuevos usuarios/ítems), sampling estratificado para validación.
- Fuente de datos: MovieLens (GroupLens).

## Licencia

Este proyecto se rige por la licencia MIT del repositorio. Consulta el archivo LICENSE en la raíz.
