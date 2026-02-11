# Proyecto 5: Clasificación de Imágenes de Residuos (PyTorch)

## Descripción

Clasificación de imágenes de residuos (vidrio, papel, cartón, plástico, metal y basura) con modelos de Deep Learning en PyTorch. El dataset está en [data/dataset-resized](file:///d:/GitHub/Ruta_aprendizaje_2024/03-Aplicación_de_Modelos/Proyecto_5/data/dataset-resized) y las dimensiones se configuran en [constants.py](file:///d:/GitHub/Ruta_aprendizaje_2024/03-Aplicación_de_Modelos/Proyecto_5/src/utils/constants.py).

## Estructura

```
Proyecto_5/
├── data/
│   └── dataset-resized/
│       ├── glass/ paper/ cardboard/ plastic/ metal/ trash/
├── docs/
│   ├── one-indexed-files-notrash_train.txt
│   ├── one-indexed-files-notrash_val.txt
│   └── one-indexed-files-notrash_test.txt
├── notebooks/
│   ├── 01_ingesta_seleccion_indices.ipynb
│   ├── 02_eda_imagenes.ipynb
│   ├── 03_preparacion_datos.ipynb
│   ├── 04_modelo_baseline_cnn.ipynb
│   ├── 05_transfer_learning_resnet.ipynb
│   └── 06_evaluacion_metricas.ipynb
├── src/
│   ├── __init__.py
│   ├── dataset.py
│   ├── train_cnn.py
│   └── utils/
│       ├── constants.py
│       └── resize.py
└── requirements.txt
```

## Requerimientos de Instalación

Instalar desde [requirements.txt](file:///d:/GitHub/Ruta_aprendizaje_2024/03-Aplicación_de_Modelos/Proyecto_5/requirements.txt):
```bash
pip install -r requirements.txt
```

## Uso

- El dataset ya está organizado en `data/dataset-resized/` por carpetas de clase.
- Las dimensiones de redimensionado se ajustan en `src/utils/constants.py` (DIM1, DIM2).
- Los splits de train/val/test se toman de los archivos en `docs/`.
- Ejecutar los cuadernos en orden (01 → 06) para carga, análisis, preparación, entrenamiento y evaluación.

## Información Relacionada

- Técnicas: CNN básica y transferencia de aprendizaje con ResNet18 (torchvision).
- Métricas: Accuracy, F1, matriz de confusión, Precision/Recall por clase.
