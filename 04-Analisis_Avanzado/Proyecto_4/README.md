# Análisis de Texto Jurídico (EUR-Lex)

## Descripción del Proyecto

Este proyecto aplica técnicas avanzadas de Procesamiento de Lenguaje Natural (NLP) para entender, procesar y extraer información valiosa de documentos legales a gran escala. Utilizando el corpus de la Unión Europea (EUR-Lex), se abordan tareas que van desde la exploración inicial y limpieza de textos hasta el reconocimiento de entidades (NER), clasificación automática, modelado de tópicos y búsqueda semántica por similitud.

## Dataset

- **Nombre:** EurlexResources (A Corpus Covering the Largest EURLEX Resources)
- **Fuente:** Hugging Face (joelniklaus/eurlex_resources)
- **URL:** [https://huggingface.co/datasets/joelniklaus/eurlex_resources](https://huggingface.co/datasets/joelniklaus/eurlex_resources)
- **Características:** Corpus masivo (~179GB) que incluye jurisprudencia (caselaw), decisiones, directivas, reglamentos y propuestas de la UE en múltiples idiomas.
- **Acceso:** Se utiliza el modo `streaming=True` de la librería `datasets` para manejar los datos sin necesidad de descarga completa.

## Estructura del Proyecto

```
Proyecto_4/
├── data/              # Carpeta para reportes o muestras locales
├── notebooks/         # Flujo de trabajo completo
│   ├── 01_carga_y_exploracion.ipynb      # Ingesta en streaming y análisis descriptivo
│   ├── 02_preprocesamiento_y_ner.ipynb   # Limpieza y extracción de entidades (NER)
│   ├── 03_clasificacion_de_documentos.ipynb # Modelos de clasificación de texto
│   ├── 04_analisis_de_topicos.ipynb      # Descubrimiento de temas (LDA)
│   └── 05_busqueda_y_similitud.ipynb     # Búsqueda semántica con Embeddings
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Documentación actual
```

## Requerimientos de Instalación

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install datasets pandas numpy matplotlib seaborn scikit-learn transformers torch sentence-transformers jupyter
```

## Flujo de Trabajo

1. **Carga y Exploración**: Uso de la API de Hugging Face para acceder a la jurisprudencia y documentos legales en tiempo real.
2. **Preprocesamiento y NER**: Limpieza de ruido textual y uso de modelos pre-entrenados (BERT/RoBERTa) para identificar organizaciones, personas y lugares.
3. **Clasificación**: Entrenamiento de clasificadores para categorizar documentos según su contenido jurídico.
4. **Análisis de Tópicos**: Aplicación de LDA para identificar los temas predominantes en el corpus legal.
5. **Búsqueda Semántica**: Implementación de un buscador que utiliza similitud del coseno sobre vectores densos para encontrar leyes o casos relacionados.

---
**Autor:** Frank Yesid
**Año:** 2025
