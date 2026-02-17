# Patrones de Consumo Energético

## Descripción del Proyecto

Este proyecto analiza patrones de consumo eléctrico en un hogar a partir de mediciones tomadas cada minuto durante casi cuatro años. El objetivo es entender cómo varía el consumo a lo largo del tiempo, identificar periodos de mayor demanda y explorar diferencias entre distintos tipos de uso eléctrico.

Se trabaja con una serie temporal multivariante que incluye medidas de potencia activa, potencia reactiva, voltaje, intensidad y submediciones por tipo de dispositivo.

## Dataset

- Nombre: Individual Household Electric Power Consumption
- Fuente: UCI Machine Learning Repository
- URL: https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption
- Licencia: Creative Commons Attribution 4.0 International (CC BY 4.0)

Características principales:

- Mediciones en un hogar ubicado en Sceaux, Francia.
- Periodo: diciembre de 2006 a noviembre de 2010 (47 meses).
- Frecuencia de muestreo: un minuto.
- Número de registros: 2 075 259.
- Tipo: serie temporal multivariante.

Variables principales:

- date: fecha en formato dd/mm/yyyy.
- time: hora en formato hh:mm:ss.
- global_active_power: potencia activa promedio por minuto en kilovatios.
- global_reactive_power: potencia reactiva promedio por minuto en kilovatios.
- voltage: voltaje promedio por minuto en voltios.
- global_intensity: intensidad de corriente promedio por minuto en amperios.
- sub_metering_1: consumo asociado principalmente a cocina.
- sub_metering_2: consumo asociado principalmente a lavandería y refrigeración.
- sub_metering_3: consumo asociado a calentador de agua eléctrico y aire acondicionado.

## Objetivos de Análisis

- Visualizar la evolución del consumo eléctrico global a distintas escalas de tiempo.
- Identificar patrones diarios, semanales y estacionales de consumo.
- Analizar la contribución de cada submedición al consumo total.
- Detectar posibles anomalías o comportamientos inusuales en la serie temporal.
- Preparar el conjunto de datos para tareas posteriores de modelado y pronóstico.

## Estructura del Proyecto

```
Proyecto_2/
├── data/
│   ├── household_power_consumption.txt
│   ├── individual+household+electric+power+consumption.zip
│   └── household_power_consumption.csv   # Archivo generado a partir de ucimlrepo
├── notebooks/
│   ├── 01_ingesta_y_limpieza.ipynb
│   ├── 02_eda_consumo_energetico.ipynb
│   ├── 03_caracteristicas_temporales.ipynb
│   └── 04_modelado_y_pronostico.ipynb
├── src/
│   └── (scripts de apoyo para carga y transformación)
├── requirements.txt
└── README.md
```

## Requerimientos de Instalación

Puedes instalar las dependencias principales con:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels jupyter ucimlrepo
```

O, desde la carpeta del proyecto:

```bash
pip install -r requirements.txt
```

## Descarga y Preparación de Datos con ucimlrepo

Para descargar el dataset directamente desde el repositorio de UCI y guardarlo como CSV en la carpeta `data`, puedes ejecutar el siguiente script desde la carpeta del proyecto:

```python
from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo


def descargar_y_guardar_dataset():
    dataset = fetch_ucirepo(id=235)
    X = dataset.data.features
    y = dataset.data.targets
    df = pd.concat([X, y], axis=1)
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    output_path = data_dir / "household_power_consumption.csv"
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    descargar_y_guardar_dataset()
```

Después de ejecutar este script, tendrás disponible el archivo:

- `data/household_power_consumption.csv`

Este archivo será la base para los análisis exploratorios y modelos desarrollados en los cuadernos de la carpeta `notebooks`.

## Próximos Pasos

- Crear cuadernos de Jupyter para:
  - Ingesta y limpieza de datos.
  - Análisis exploratorio de consumo energético.
  - Ingeniería de características temporales.
  - Modelado y pronóstico del consumo.
- Integrar visualizaciones avanzadas para comunicar patrones y hallazgos clave.
