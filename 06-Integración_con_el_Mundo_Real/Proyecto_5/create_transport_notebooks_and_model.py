from pathlib import Path
import json
import math
import warnings

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

warnings.filterwarnings("ignore")

PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "public_transport_delays.csv"
NOTEBOOK_DIR = PROJECT_DIR / "notebook"
REPORT_DIR = PROJECT_DIR / "documents" / "informe_descriptiva"
MODEL_DIR = PROJECT_DIR / "models"

for path in [NOTEBOOK_DIR, REPORT_DIR, MODEL_DIR]:
    path.mkdir(parents=True, exist_ok=True)


def create_notebook(cells, path):
    try:
        import nbformat
        from nbformat.v4 import new_notebook
        nb = new_notebook(cells=cells)
        nb.metadata = {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        }
        with open(path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
    except Exception:
        # Fallback simple JSON structure if nbformat is unavailable
        payload = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.11"}}, "nbformat": 4, "nbformat_minor": 5}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=1, ensure_ascii=False)


def add_cell(cells, source, cell_type="code"):
    if cell_type == "markdown":
        cells.append({"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)})
    else:
        cells.append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source.splitlines(keepends=True)})


def make_notebook_1(df):
    cells = []
    add_cell(cells, "# 01. Carga y análisis inicial\n\nEste cuaderno revisa la estructura del dataset, la calidad de los datos, la distribución de variables y los patrones iniciales para entender el problema de retrasos del transporte público.", "markdown")
    add_cell(cells, "import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom pathlib import Path\n\nplt.style.use('seaborn-v0_8-darkgrid')\n\ndf = pd.read_csv(Path('data/public_transport_delays.csv'))\ndf.head()", "code")
    add_cell(cells, "## Vista general del dataset\n\nEn esta sección se revisa el tamaño del conjunto, los tipos de datos y la presencia de valores faltantes.", "markdown")
    add_cell(cells, "print('Filas:', df.shape[0])\nprint('Columnas:', df.shape[1])\nprint('\\nTipos de datos:')\nprint(df.dtypes)\nprint('\\nValores faltantes:')\nprint(df.isna().sum())", "code")
    add_cell(cells, "## Distribución de la variable objetivo\n\nLa columna delayed representa si el viaje terminó retrasado o no. Este balance es clave para interpretar los resultados del modelo.", "markdown")
    add_cell(cells, "target_dist = df['delayed'].value_counts().rename(index={1:'Retrasado', 0:'No retrasado'})\nax = target_dist.plot(kind='bar', color=['#4C78A8', '#F58518'], edgecolor='black')\nax.set_title('Distribución de la variable delayed')\nax.set_ylabel('Frecuencia')\nax.set_xlabel('Clase')\nplt.xticks(rotation=0)\nplt.tight_layout()\nplt.show()", "code")
    add_cell(cells, "## Distribuciones numéricas\n\nSe inspeccionan las distribuciones de las variables numéricas para detectar sesgos, valores extremos o comportamientos particulares.", "markdown")
    add_cell(cells, "num_cols = ['actual_departure_delay_min', 'actual_arrival_delay_min', 'temperature_C', 'humidity_percent', 'wind_speed_kmh', 'precipitation_mm', 'event_attendance_est', 'traffic_congestion_index']\nfig, axes = plt.subplots(2, 4, figsize=(16, 8))\naxes = axes.flatten()\nfor ax, col in zip(axes, num_cols):\n    sns.histplot(df[col], bins=25, kde=True, ax=ax, color='#4C78A8')\n    ax.set_title(col)\nfig.tight_layout()\nplt.show()", "code")
    add_cell(cells, "## Análisis exploratorio por categorías\n\nSe comparan las proporciones de retrasos según transporte, clima, eventos y horarios.", "markdown")
    add_cell(cells, "fig, axes = plt.subplots(2, 2, figsize=(14, 8))\n\nsns.countplot(data=df, x='transport_type', hue='delayed', ax=axes[0, 0], palette=['#4C78A8', '#F58518'])\naxes[0, 0].set_title('Retrasos por tipo de transporte')\n\nsns.countplot(data=df, x='weather_condition', hue='delayed', ax=axes[0, 1], palette=['#4C78A8', '#F58518'])\naxes[0, 1].set_title('Retrasos por condición climática')\naxes[0, 1].tick_params(axis='x', rotation=45)\n\nsns.countplot(data=df, x='event_type', hue='delayed', ax=axes[1, 0], palette=['#4C78A8', '#F58518'])\naxes[1, 0].set_title('Retrasos por tipo de evento')\naxes[1, 0].tick_params(axis='x', rotation=45)\n\nsns.countplot(data=df, x='peak_hour', hue='delayed', ax=axes[1, 1], palette=['#4C78A8', '#F58518'])\naxes[1, 1].set_title('Retrasos por hora pico')\n\nfig.tight_layout()\nplt.show()", "code")
    add_cell(cells, "### Resumen del notebook 1\n\nEste primer análisis confirma que el problema es de clasificación binaria con un desbalance notable, además de mostrar que las variables de contexto y de servicio parecen estar asociadas con la ocurrencia de retrasos.", "markdown")
    return cells


def make_notebook_2(df):
    cells = []
    add_cell(cells, "# 02. Descriptiva detallada y extracción de características\n\nEste cuaderno transforma la información original en variables útiles para modelar, y revisa la relación entre estas nuevas variables y la ocurrencia de retrasos.", "markdown")
    add_cell(cells, "import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom pathlib import Path\n\nplt.style.use('seaborn-v0_8-darkgrid')\ndf = pd.read_csv(Path('data/public_transport_delays.csv'))\n\ndf['event_type'] = df['event_type'].fillna('Sin evento')\ndf['event_presence'] = (df['event_type'] != 'Sin evento').astype(int)\ndf['date'] = pd.to_datetime(df['date'])\ndf['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')\ndf['hour'] = df['time'].dt.hour\ndf['day_of_week'] = df['date'].dt.dayofweek\ndf['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)\n\ndf['scheduled_departure_dt'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['scheduled_departure'])\ndf['scheduled_arrival_dt'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['scheduled_arrival'])\ndf['scheduled_trip_duration_min'] = (df['scheduled_arrival_dt'] - df['scheduled_departure_dt']).dt.total_seconds() / 60\ndf['delay_gap_min'] = df['actual_arrival_delay_min'] - df['actual_departure_delay_min']\n\ndf[['hour', 'day_of_week', 'is_weekend', 'event_presence', 'scheduled_trip_duration_min', 'delay_gap_min']].head()", "code")
    add_cell(cells, "## Estadísticas descriptivas por categoría\n\nSe resumen las principales métricas para detectar diferencias entre grupos y confirmar qué variables aportan contexto al retraso.", "markdown")
    add_cell(cells, "summary = df.groupby('transport_type').agg(\n    retrasos=('delayed', 'mean'),\n    viajes=('trip_id', 'count'),\n    temperatura_prom=('temperature_C', 'mean'),\n    congestion_prom=('traffic_congestion_index', 'mean')\n).reset_index()\nsummary", "code")
    add_cell(cells, "## Relación entre variables y retrasos\n\nSe calculan medias y proporciones para cuantificar cómo cambian los retrasos según condiciones externas y del servicio.", "markdown")
    add_cell(cells, "grouped_weather = df.groupby('weather_condition')['delayed'].mean().sort_values(ascending=False)\ngrouped_event = df.groupby('event_presence')['delayed'].mean()\nfig, axes = plt.subplots(1, 2, figsize=(12, 4))\ngrouped_weather.plot(kind='bar', ax=axes[0], color='#4C78A8')\naxes[0].set_title('Probabilidad de retraso por clima')\naxes[0].set_ylabel('Proporción')\n\ngrouped_event.plot(kind='bar', ax=axes[1], color=['#F58518', '#4C78A8'])\naxes[1].set_title('Probabilidad de retraso con/sin evento')\naxes[1].set_ylabel('Proporción')\nfig.tight_layout()\nplt.show()", "code")
    add_cell(cells, "## Matriz de correlación\n\nPara identificar variables de interés, se construye una matriz con variables numéricas y con representaciones binarias de variables categóricas.", "markdown")
    add_cell(cells, "feature_frame = df[['delayed', 'actual_departure_delay_min', 'actual_arrival_delay_min', 'temperature_C', 'humidity_percent', 'wind_speed_kmh', 'precipitation_mm', 'event_attendance_est', 'traffic_congestion_index', 'holiday', 'peak_hour', 'weekday', 'hour', 'day_of_week', 'is_weekend', 'event_presence', 'scheduled_trip_duration_min', 'delay_gap_min']]\nfeature_frame = pd.get_dummies(feature_frame, columns=['weekday'], prefix='weekday')\ncorrelation = feature_frame.corr(numeric_only=True)\nplt.figure(figsize=(14, 10))\nsns.heatmap(correlation, cmap='coolwarm', center=0, annot=False)\nplt.title('Matriz de correlación de variables de interés')\nplt.tight_layout()\nplt.show()", "code")
    add_cell(cells, "## Variables de interés para el modelo\n\nSe identifican las variables más prometedoras para el entrenamiento: condiciones climáticas, congestión, eventos, hora y duración programada del viaje.", "markdown")
    add_cell(cells, "corr_with_target = correlation['delayed'].drop('delayed').sort_values(ascending=False)\ncorr_with_target.head(10)", "code")
    add_cell(cells, "### Resumen del notebook 2\n\nLa ingeniería de características permitió convertir el contexto temporal y operativo en variables más informativas, y la matriz de correlación evidenció que la congestión, los retrasos anteriores, la presencia de eventos y la hora del día son variables de alto interés.", "markdown")
    return cells


def make_notebook_3(df):
    cells = []
    add_cell(cells, "# 03. Entrenamiento de un modelo predictivo\n\nEste cuaderno entrena un clasificador para predecir si un viaje terminará retrasado, usando variables de contexto, clima, eventos y programación.", "markdown")
    add_cell(cells, "import json\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom pathlib import Path\nfrom sklearn.compose import ColumnTransformer\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.impute import SimpleImputer\nfrom sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import OneHotEncoder\nimport joblib\n\nplt.style.use('seaborn-v0_8-darkgrid')\ndf = pd.read_csv(Path('data/public_transport_delays.csv'))\n\ndf['event_type'] = df['event_type'].fillna('Sin evento')\ndf['event_presence'] = (df['event_type'] != 'Sin evento').astype(int)\ndf['date'] = pd.to_datetime(df['date'])\ndf['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')\ndf['hour'] = df['time'].dt.hour\ndf['day_of_week'] = df['date'].dt.dayofweek\ndf['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)\n\ndf['scheduled_departure_dt'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['scheduled_departure'])\ndf['scheduled_arrival_dt'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['scheduled_arrival'])\ndf['scheduled_trip_duration_min'] = (df['scheduled_arrival_dt'] - df['scheduled_departure_dt']).dt.total_seconds() / 60\ndf['delay_gap_min'] = df['actual_arrival_delay_min'] - df['actual_departure_delay_min']\n\nfeature_columns = [\n    'transport_type', 'weather_condition', 'event_type', 'season', 'holiday', 'peak_hour', 'is_weekend',\n    'hour', 'day_of_week', 'traffic_congestion_index', 'temperature_C', 'humidity_percent',\n    'wind_speed_kmh', 'precipitation_mm', 'event_attendance_est', 'scheduled_trip_duration_min',\n    'actual_departure_delay_min', 'actual_arrival_delay_min', 'delay_gap_min'\n]\n\nX = df[feature_columns]\ny = df['delayed']\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42, stratify=y\n)\n\nnum_features = [\n    'traffic_congestion_index', 'temperature_C', 'humidity_percent', 'wind_speed_kmh',\n    'precipitation_mm', 'event_attendance_est', 'scheduled_trip_duration_min',\n    'actual_departure_delay_min', 'actual_arrival_delay_min', 'delay_gap_min', 'hour', 'day_of_week'\n]\ncat_features = [\n    'transport_type', 'weather_condition', 'event_type', 'season', 'holiday', 'peak_hour', 'is_weekend'\n]\n\npreprocess = ColumnTransformer(\n    transformers=[\n        ('num', Pipeline([('imputer', SimpleImputer(strategy='median'))]), num_features),\n        ('cat', Pipeline([('imputer', SimpleImputer(strategy='most_frequent')), ('onehot', OneHotEncoder(handle_unknown='ignore'))]), cat_features),\n    ]\n)\n\nmodel = Pipeline([\n    ('preprocess', preprocess),\n    ('classifier', RandomForestClassifier(n_estimators=250, max_depth=12, random_state=42))\n])\n\nmodel.fit(X_train, y_train)\npred = model.predict(X_test)\n\nmetrics = {\n    'accuracy': round(accuracy_score(y_test, pred), 4),\n    'precision': round(precision_score(y_test, pred), 4),\n    'recall': round(recall_score(y_test, pred), 4),\n    'f1': round(f1_score(y_test, pred), 4),\n    'roc_auc': round(roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]), 4),\n}\nmetrics", "code")
    add_cell(cells, "## Evaluación del modelo\n\nSe revisan métricas de desempeño y la matriz de confusión para interpretar el rendimiento del clasificador.", "markdown")
    add_cell(cells, "cm = confusion_matrix(y_test, pred)\nfig, ax = plt.subplots(figsize=(5, 4))\nsns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No retraso', 'Retraso'], yticklabels=['No retraso', 'Retraso'], ax=ax)\nax.set_title('Matriz de confusión')\nax.set_xlabel('Predicción')\nax.set_ylabel('Real')\nplt.tight_layout()\nplt.show()\n\nmetrics", "code")
    add_cell(cells, "## Guardado del modelo\n\nEl pipeline entrenado se serializa para reutilizarlo en nuevas predicciones.", "markdown")
    add_cell(cells, "model_path = Path('models/public_transport_delay_model.joblib')\nmodel_path.parent.mkdir(parents=True, exist_ok=True)\njoblib.dump(model, model_path)\nwith open(Path('models/model_metrics.json'), 'w', encoding='utf-8') as f:\n    json.dump(metrics, f, indent=2)\n\nprint('Modelo guardado en:', model_path)\nprint('Métricas guardadas en:', Path('models/model_metrics.json'))", "code")
    add_cell(cells, "### Resumen del notebook 3\n\nEl entrenamiento produjo un clasificador capaz de predecir si un viaje terminará retrasado con métricas útiles para evaluación. El modelo entrenado quedó guardado para uso posterior.", "markdown")
    return cells


def save_html_report(df):
    report_path = REPORT_DIR / "public_transport_delays_descriptiva.html"
    report_dir = REPORT_DIR
    report_dir.mkdir(parents=True, exist_ok=True)

    numeric_cols = ['actual_departure_delay_min', 'actual_arrival_delay_min', 'temperature_C', 'humidity_percent', 'wind_speed_kmh', 'precipitation_mm', 'event_attendance_est', 'traffic_congestion_index']
    summary = df[numeric_cols].describe().T[['mean', 'std', 'min', 'max']]

    plt.figure(figsize=(10, 4))
    sns.countplot(data=df, x='transport_type', hue='delayed', palette=['#4C78A8', '#F58518'])
    plt.title('Retrasos por tipo de transporte')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(report_dir / 'transport_type_delay.png', dpi=150)
    plt.close()

    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df, x='delayed', y='traffic_congestion_index', palette=['#4C78A8', '#F58518'])
    plt.title('Congestión por estado de retraso')
    plt.tight_layout()
    plt.savefig(report_dir / 'congestion_delay.png', dpi=150)
    plt.close()

    plt.figure(figsize=(8, 4))
    sns.barplot(data=df, x='weather_condition', y='delayed', estimator='mean', palette='viridis')
    plt.title('Probabilidad de retraso por clima')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(report_dir / 'weather_delay.png', dpi=150)
    plt.close()

    html = f"""<!DOCTYPE html>
<html lang='es'>
<head>
  <meta charset='UTF-8'>
  <title>Informe descriptivo - Public Transport Delays</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; color: #222; }}
    h1, h2 {{ color: #1f4e79; }}
    table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
    th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
    th {{ background-color: #f2f2f2; }}
    img {{ width: 100%; max-width: 700px; border: 1px solid #ddd; margin-top: 12px; }}
  </style>
</head>
<body>
  <h1>Informe descriptivo - Public Transport Delays</h1>
  <p>Este informe resume la distribución inicial, los patrones por categoría y la relación de las variables con la variable objetivo delayed.</p>

  <h2>Resumen del dataset</h2>
  <p><strong>Filas:</strong> {len(df)}<br>
  <strong>Columnas:</strong> {df.shape[1]}<br>
  <strong>Proporción de retrasos:</strong> {df['delayed'].mean():.2%}</p>

  <h2>Estadísticas descriptivas de variables numéricas</h2>
  {summary.to_html()} 

  <h2>Visualizaciones clave</h2>
  <img src='transport_type_delay.png' alt='Retrasos por tipo de transporte'>
  <img src='congestion_delay.png' alt='Congestión por estado de retraso'>
  <img src='weather_delay.png' alt='Probabilidad de retraso por clima'>

  <h2>Observaciones</h2>
  <ul>
    <li>La tasa de retraso es alta y el problema muestra un patrón de clasificación útil para entrenamiento.</li>
    <li>La congestión y las condiciones climáticas parecen influir de forma relevante en la probabilidad de retraso.</li>
    <li>La presencia de eventos y el tipo de transporte aportan contexto adicional para el modelo.</li>
  </ul>
</body>
</html>
"""
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html)


def main():
    df = pd.read_csv(DATA_PATH)
    df['event_type'] = df['event_type'].fillna('Sin evento')
    df['event_presence'] = (df['event_type'] != 'Sin evento').astype(int)
    df['date'] = pd.to_datetime(df['date'])
    df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')
    df['hour'] = df['time'].dt.hour
    df['day_of_week'] = df['date'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['scheduled_departure_dt'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['scheduled_departure'])
    df['scheduled_arrival_dt'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['scheduled_arrival'])
    df['scheduled_trip_duration_min'] = (df['scheduled_arrival_dt'] - df['scheduled_departure_dt']).dt.total_seconds() / 60
    df['delay_gap_min'] = df['actual_arrival_delay_min'] - df['actual_departure_delay_min']

    notebook_1 = make_notebook_1(df)
    notebook_2 = make_notebook_2(df)
    notebook_3 = make_notebook_3(df)

    create_notebook(notebook_1, NOTEBOOK_DIR / '01_carga_analisis_inicial.ipynb')
    create_notebook(notebook_2, NOTEBOOK_DIR / '02_descriptiva_caracteristicas.ipynb')
    create_notebook(notebook_3, NOTEBOOK_DIR / '03_entrenamiento_modelo.ipynb')

    save_html_report(df)

    feature_columns = [
        'transport_type', 'weather_condition', 'event_type', 'season', 'holiday', 'peak_hour', 'is_weekend',
        'hour', 'day_of_week', 'traffic_congestion_index', 'temperature_C', 'humidity_percent',
        'wind_speed_kmh', 'precipitation_mm', 'event_attendance_est', 'scheduled_trip_duration_min',
        'actual_departure_delay_min', 'actual_arrival_delay_min', 'delay_gap_min'
    ]
    X = df[feature_columns]
    y = df['delayed']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    num_features = [
        'traffic_congestion_index', 'temperature_C', 'humidity_percent', 'wind_speed_kmh',
        'precipitation_mm', 'event_attendance_est', 'scheduled_trip_duration_min',
        'actual_departure_delay_min', 'actual_arrival_delay_min', 'delay_gap_min', 'hour', 'day_of_week'
    ]
    cat_features = ['transport_type', 'weather_condition', 'event_type', 'season', 'holiday', 'peak_hour', 'is_weekend']

    preprocess = ColumnTransformer(
        transformers=[
            ('num', Pipeline([('imputer', SimpleImputer(strategy='median'))]), num_features),
            ('cat', Pipeline([('imputer', SimpleImputer(strategy='most_frequent')), ('onehot', OneHotEncoder(handle_unknown='ignore'))]), cat_features),
        ]
    )

    model = Pipeline([
        ('preprocess', preprocess),
        ('classifier', RandomForestClassifier(n_estimators=250, max_depth=12, random_state=42))
    ])
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    metrics = {
        'accuracy': round(accuracy_score(y_test, pred), 4),
        'precision': round(precision_score(y_test, pred), 4),
        'recall': round(recall_score(y_test, pred), 4),
        'f1': round(f1_score(y_test, pred), 4),
        'roc_auc': round(roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]), 4),
    }

    model_path = MODEL_DIR / 'public_transport_delay_model.joblib'
    joblib.dump(model, model_path)
    with open(MODEL_DIR / 'model_metrics.json', 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=2)

    print('Notebook 1 created:', NOTEBOOK_DIR / '01_carga_analisis_inicial.ipynb')
    print('Notebook 2 created:', NOTEBOOK_DIR / '02_descriptiva_caracteristicas.ipynb')
    print('Notebook 3 created:', NOTEBOOK_DIR / '03_entrenamiento_modelo.ipynb')
    print('HTML report created:', REPORT_DIR / 'public_transport_delays_descriptiva.html')
    print('Model saved:', model_path)
    print('Metrics:', metrics)


if __name__ == '__main__':
    main()
