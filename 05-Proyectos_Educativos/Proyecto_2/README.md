# Retos de Limpieza de Datos (Data Cleaning)

## Descripción del Proyecto

Este proyecto educativo está diseñado para practicar una de las tareas más críticas en la ciencia de datos: la **limpieza y preparación de datos**. Se utiliza un dataset real sobre las giras musicales más exitosas de la historia, el cual presenta múltiples problemas de calidad que deben ser resueltos para realizar análisis posteriores precisos.

El enfoque es el desarrollo de habilidades para identificar e implementar soluciones a problemas comunes como valores nulos, formatos de moneda inconsistentes, caracteres especiales, y errores de tipografía.

## Dataset

- **Nombre:** Dirty Dataset to Practice Data Cleaning
- **Fuente:** [Amrutha Yenikonda / Kaggle](https://www.kaggle.com/datasets/amruthayenikonda/dirty-dataset-to-practice-data-cleaning)
- **Archivo Local:** `data/my_file (1).csv`
- **Contenido:** 
  - Estadísticas de giras mundiales de artistas como Taylor Swift, Beyoncé, Madonna, etc.
  - Columnas con ingresos brutos (ajustados y reales), años de gira, número de shows y rankings.
- **Problemas de Calidad Identificados:**
  - Símbolos de moneda (`$`) y comas intercalados en valores numéricos.
  - Referencias bibliográficas entre corchetes (ej. `[1]`, `[a]`) dentro de los datos.
  - Caracteres especiales como cruces (`†`, `‡`) y asteriscos (`*`).
  - Formatos de fecha y rangos de años inconsistentes.
  - Valores faltantes en rankings y estadísticas secundarias.

## Estructura del Proyecto

```
Proyecto_2/
├── data/                  # Archivos de datos originales y procesados
│   ├── my_file (1).csv    # Dataset original "sucio"
│   └── music_tours_cleaned.csv # Resultado final de la limpieza
├── notebooks/             # Retos de limpieza paso a paso
│   ├── 01_exploracion_inicial.ipynb # Identificación de problemas de calidad
│   └── 02_limpieza_y_normalizacion.ipynb # Transformación y corrección de datos
├── requirements.txt       # Dependencias necesarias (pandas, re, etc.)
└── README.md              # Documentación actual
```

## Requerimientos de Instalación

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

## Objetivos del Reto

1.  **Diagnóstico de Calidad**: Aprender a utilizar `pandas` para identificar inconsistencias estructurales y de contenido.
2.  **Expresiones Regulares (Regex)**: Utilizar el módulo `re` de Python para limpiar cadenas de texto complejas y extraer valores numéricos.
3.  **Normalización de Formatos**: Convertir columnas de ingresos y fechas en tipos de datos adecuados para el análisis numérico.
4.  **Tratamiento de Nulos**: Implementar estrategias de imputación o eliminación de valores faltantes basadas en el contexto de los datos.

---
**Autor:** Frank Yesid
**Año:** 2025
