# Simulación de Pandemias (Modelo SIR)

## Descripción del Proyecto

Este proyecto educativo tiene como objetivo comprender la dinámica de propagación de enfermedades infecciosas mediante el uso de modelos matemáticos epidemiológicos. Se utiliza el dataset oficial de la **Universidad Johns Hopkins (JHU)**, que recopila series temporales mundiales de casos de COVID-19 entre 2020 y 2023.

El enfoque principal es el ajuste del **Modelo SIR (Susceptibles, Infectados, Recuperados)** a los picos reales observados en los datos para calcular parámetros clave como la tasa de transmisión ($\beta$), la tasa de recuperación ($\gamma$) y el número reproductivo básico ($R_0$).

## Dataset

- **Nombre:** Johns Hopkins COVID-19 Time Series Data
- **Fuente:** [CSSEGISandData/COVID-19 (GitHub)](https://github.com/CSSEGISandData/COVID-19)
- **Características:** 
  - Series diarias mundiales de casos confirmados, muertes y recuperados.
  - Desglose por país y región/provincia.
  - Periodo: Enero 2020 - Marzo 2023.
  - Volumen: ~1 millón de registros tras procesamiento.

## Estructura del Proyecto

```
Proyecto_1/
├── data/              # Datos procesados en formato largo (long format)
├── notebooks/         # Flujo de trabajo educativo
│   ├── 01_ingesta_y_limpieza.ipynb      # Descarga y transformación de datos (JHU API)
│   ├── 02_eda_y_visualizacion.ipynb    # Análisis de tendencias y picos globales
│   └── 03_modelo_sir.ipynb            # Implementación y ajuste del modelo SIR
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Documentación actual
```

## Requerimientos de Instalación

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

## Objetivos Educativos

1.  **Manipulación de Series Temporales**: Aprender a transformar datos complejos de formato ancho a largo para análisis temporal.
2.  **Modelado Epidemiológico**: Implementar el sistema de ecuaciones diferenciales del modelo SIR usando `scipy.integrate.odeint`.
3.  **Optimización de Parámetros**: Ajustar modelos teóricos a datos reales mediante técnicas de minimización de errores (`scipy.optimize.minimize`).
4.  **Interpretación de Resultados**: Entender el significado biológico y social de parámetros como $R_0$ en el contexto de una pandemia real.

---
**Autor:** Frank Yesid
**Año:** 2025
