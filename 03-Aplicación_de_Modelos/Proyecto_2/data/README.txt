Vehicle Routing Problem (VRP) - Dataset

Origen:
- Kaggle: Vehicle Routing Problem GA Dataset
- URL: https://www.kaggle.com/datasets/abhilashg23/vehicle-routing-problem-ga-dataset?resource=download

Archivo:
- VRP.csv

Contenido esperado:
- Coordenadas de clientes (X/Y o lat/lon)
- Demanda por cliente
- Capacidad de vehículo(s)
- Depósito (índice o coordenadas)
- (Opcional) Ventanas de tiempo, matrices de distancia, costos

Notas:
- Si el archivo provee matriz de distancias, se usarán directamente; en caso contrario se construirá con Euclídea a partir de coordenadas.
- Ver notebooks de 01_ingesta_estandarizacion y 03_modelo_or_tools.
