# Clasificación para Reciclaje

## Descripción

Clasificación de imágenes de residuos (plástico, papel, vidrio, etc.) mediante modelos de visión por computadora.

## Estructura Sugerida

```
Proyecto_5/
├── data/                      # Imágenes etiquetadas por tipo de residuo
├── notebooks/
│   ├── 01_eda_imagenes.ipynb
│   ├── 02_entrenamiento_cnn.ipynb
│   └── 03_evaluacion_modelo.ipynb
├── src/
│   ├── dataset.py
│   └── train_cnn.py
└── README.md
```

## Requerimientos de Instalación

```bash
pip install numpy pandas scikit-learn opencv-python matplotlib seaborn jupyter tensorflow
```
Opcional (PyTorch):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

## Uso

- Organiza imágenes en `data/` por carpetas de clase.
- Ejecuta los cuadernos para preprocesamiento, entrenamiento y evaluación.

## Información Relacionada

- Técnicas: CNN (ConvNets), aumento de datos, transferencia de aprendizaje.
- Métricas: Accuracy, F1, matriz de confusión, Precision/Recall por clase.

