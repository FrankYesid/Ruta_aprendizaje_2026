# Detección de Anomalías en ECG

## Descripción del Proyecto
Este proyecto tiene como objetivo la detección de anomalías en electrocardiogramas (ECG) mediante el uso de modelos de clasificación de Machine Learning e implementación en dispositivos Edge. Se emplea la base de datos MIT-BIH Arrhythmia y herramientas de análisis avanzadas para identificar patrones asociados a enfermedades cardiovasculares (ECV).

## Sobre la Base de Datos
Los datos utilizados provienen del servicio PhysioNet y han sido extraídos de la base de datos MIT-BIH Arrhythmia. Las características principales de los datos son:

- ECG de 45 pacientes (19 mujeres y 26 hombres, edades entre 23-89 años).
- 17 clases diferentes, incluyendo ritmo sinusal normal y 15 tipos de disfunciones cardíacas.
- Señales registradas a una frecuencia de muestreo de 360 Hz y una ganancia de 200 adu/mV.
- 1000 fragmentos de 10 segundos seleccionados aleatoriamente.
- Se utiliza una única derivación (MLII).
- Formato de los datos en `.mat` (Matlab).

### Fuente de Datos
- Base de datos: [MIT-BIH Arrhythmia](https://data.mendeley.com/datasets/7dybx7wyfn/3)
- Artículo de referencia: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0957417417306292?via%3Dihub)

## Enfermedades Cardiovasculares (ECV)
Las enfermedades cardiovasculares son una de las principales causas de morbilidad y mortalidad en el mundo. Algunas de las más comunes incluyen:

- **Enfermedad coronaria**: acumulación de placa en arterias del corazón.
- **Infarto de miocardio**: obstrucción de una arteria coronaria.
- **Insuficiencia cardíaca**: incapacidad del corazón para bombear sangre adecuadamente.
- **Hipertensión arterial**: presión sanguínea elevada.
- **Accidente cerebrovascular**: interrupción del flujo sanguíneo al cerebro.
- **Arritmias cardíacas**: alteraciones en el ritmo del corazón.
- **Enfermedades valvulares**: mal funcionamiento de las válvulas del corazón.
- **Cardiopatías congénitas**: anomalías estructurales presentes desde el nacimiento.

Los factores de riesgo incluyen hipertensión, colesterol alto, tabaquismo, obesidad, diabetes y falta de actividad física.

## Solución Planteada
Se propone la implementación de un clasificador de ECG en un microcontrolador como un **wearable** para pacientes hospitalizados con alguna enfermedad cardiovascular. Este sistema permitirá la detección de anomalías en tiempo real y la generación de alarmas automáticas para el personal médico cuando se identifique una irregularidad en el ritmo cardíaco.

## Herramientas Utilizadas
- **Python y Jupyter Notebooks** para el análisis de datos.
- **Bibliotecas de Machine Learning** como TensorFlow, Scikit-Learn y PyTorch.
- **Procesamiento de señales con SciPy y NumPy**.
- **Edge Impulse** para la implementación en dispositivos embebidos.

## Requerimientos de Instalación

Instala las dependencias principales:
```bash
pip install numpy scipy scikit-learn matplotlib seaborn jupyter tensorflow
```
Opcional (alternativa a TensorFlow):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

## Instrucciones de Uso
1. Descargar y cargar los datos desde los enlaces proporcionados.
2. Ejecutar los notebooks de preprocesamiento y entrenamiento.
3. Evaluar el rendimiento del modelo.
4. Implementar el modelo en hardware para pruebas en tiempo real.

## Contribuciones
Cualquier contribución es bienvenida. Puedes enviar un pull request con mejoras en el código, optimización del modelo o nuevas funcionalidades para el sistema de detección en Edge.

## Contacto
Para más información, por favor contacta a Frank Yesid o visita el repositorio del proyecto.

---
