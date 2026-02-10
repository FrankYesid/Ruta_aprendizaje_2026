# Dataset Boston Housing

## Información General

**Nombre**: Boston Housing Dataset
**Archivo**: BostonHousing.csv
**Origen**: Dataset clásico de machine learning, disponible en UCI Machine Learning Repository
**Tamaño**: 506 registros, 14 columnas
**Tipo de Problema**: Regresión (predicción de precios de viviendas)

## Descripción de Variables

### Variables de Entrada (Características)

1. **CRIM** - Tasa de criminalidad per cápita por ciudad
   - Rango: 0.00632 - 88.9762
   - Tipo: Continua
   - Descripción: Nivel de criminalidad en el área

2. **ZN** - Proporción de terrenos residenciales zonificados para lotes de más de 25,000 pies cuadrados
   - Rango: 0 - 100
   - Tipo: Continua
   - Descripción: Zonificación de terrenos grandes

3. **INDUS** - Proporción de acres de negocios no minoristas por ciudad
   - Rango: 0.46 - 27.74
   - Tipo: Continua
   - Descripción: Industrialización del área

4. **CHAS** - Variable ficticia de Charles River
   - Valores: 0 o 1
   - Tipo: Binaria
   - Descripción: 1 si el tracto limita con el río Charles; 0 en caso contrario

5. **NOX** - Concentración de óxidos nítricos (partes por 10 millones)
   - Rango: 0.385 - 0.871
   - Tipo: Continua
   - Descripción: Nivel de contaminación del aire

6. **RM** - Número promedio de habitaciones por vivienda
   - Rango: 3.561 - 8.78
   - Tipo: Continua
   - Descripción: Tamaño de las viviendas

7. **AGE** - Proporción de unidades ocupadas por sus propietarios construidas antes de 1940
   - Rango: 2.9 - 100
   - Tipo: Continua
   - Descripción: Antigüedad de las viviendas

8. **DIS** - Distancias ponderadas a cinco centros de empleo de Boston
   - Rango: 1.1296 - 12.1265
   - Tipo: Continua
   - Descripción: Accesibilidad al empleo

9. **RAD** - Índice de accesibilidad a carreteras radiales
   - Rango: 1 - 24
   - Tipo: Discreta
   - Descripción: Accesibilidad a carreteras principales

10. **TAX** - Tasa de impuesto a la propiedad de valor completo por $10,000
    - Rango: 187 - 711
    - Tipo: Continua
    - Descripción: Impuestos a la propiedad

11. **PTRATIO** - Proporción alumno-maestro por ciudad
    - Rango: 12.6 - 22.0
    - Tipo: Continua
    - Descripción: Calidad de las escuelas

12. **B** - 1000(Bk - 0.63)^2 donde Bk es la proporción de negros por ciudad
    - Rango: 0.32 - 396.9
    - Tipo: Continua
    - Descripción: Composición étnica (transformación aplicada)

13. **LSTAT** - Porcentaje de población de clase baja
    - Rango: 1.73 - 37.97
    - Tipo: Continua
    - Descripción: Estatus socioeconómico

### Variable Objetivo

14. **MEDV** - Valor medio de viviendas ocupadas por sus propietarios en $1000
    - Rango: 5 - 50
    - Tipo: Continua
    - Descripción: Precio medio de las viviendas (variable a predecir)

## Estadísticas del Dataset

- **Total de registros**: 506
- **Total de variables**: 14 (13 predictoras + 1 objetivo)
- **Tipo de problema**: Regresión
- **Rango de precios**: $5,000 - $50,000 (en miles de dólares de 1970)

## Calidad de Datos

- **Datos faltantes**: No hay valores faltantes
- **Outliers**: Algunas variables presentan valores atípicos
- **Escalas**: Las variables tienen diferentes escalas (requiere normalización)
- **Distribución**: Algunas variables no siguen distribución normal

## Uso en el Proyecto

Este dataset se utiliza para:
1. Práctica de técnicas de regresión
2. Comparación de modelos predictivos
3. Ingeniería de características
4. Evaluación de métricas de regresión
5. Visualización de datos

## Referencias

- Harrison, D. and Rubinfeld, D.L. `Hedonic prices and the demand for clean air', J. Environ. Economics & Management, vol.5, 81-102, 1978.
- UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Housing