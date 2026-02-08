MovieLens - Fuentes de datos

Origen:
- GroupLens MovieLens Latest: https://grouplens.org/datasets/movielens/latest/
- Small (ml-latest-small): 100,000 ratings y 3,600 tags en ~9,000 películas por ~600 usuarios (actualizado 09/2018)
- Full (ml-latest): ~33,000,000 ratings y ~2,000,000 tags en ~86,000 películas por ~330,975 usuarios; incluye tag genome (~14M relevancias en ~1,100 tags) (actualizado 09/2018)

Ubicación esperada:
- Proyecto_3/data/ml-latest-small/
  - ratings.csv
  - movies.csv
  - tags.csv
  - links.csv
- Proyecto_3/data/ml-latest/ (opcional si trabajas con el dataset completo)
  - ratings.csv
  - movies.csv
  - tags.csv
  - links.csv
  - genome-scores.csv
  - genome-tags.csv

Notas:
- Los datasets pueden cambiar con el tiempo; usa ml-latest-small para prototipos rápidos.
- Para el dataset completo, se recomienda muestrear por usuarios/películas para evitar cargas excesivas de memoria.

