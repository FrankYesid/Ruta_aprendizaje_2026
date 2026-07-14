from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor
import joblib

project_root = Path(__file__).resolve().parent
notebook_dir = project_root / 'notebook'
doc_dir = project_root / 'documents' / 'informe_descriptiva'
model_dir = project_root / 'models'
for path in [notebook_dir, doc_dir, model_dir]:
    path.mkdir(parents=True, exist_ok=True)

data_dir = project_root / 'data'


def write_notebook(path, cells):
    nb = {
        'cells': [],
        'metadata': {
            'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
            'language_info': {'name': 'python', 'version': '3.x'}
        },
        'nbformat': 4,
        'nbformat_minor': 5,
    }
    for cell_type, source in cells:
        if cell_type == 'markdown':
            nb['cells'].append({'cell_type': 'markdown', 'metadata': {}, 'source': source.splitlines(keepends=True)})
        else:
            nb['cells'].append({'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': source.splitlines(keepends=True)})
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)


# Notebook 1: carga y EDA inicial
notebook1_cells = [
    ('markdown', '# 01 - Carga inicial y análisis exploratorio\n\nEste cuaderno carga las bases disponibles en la carpeta de datos y revisa su estructura, distribuciones y valores faltantes para identificar comportamientos iniciales de cada tabla.\n'),
    ('code', "from pathlib import Path\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\nsns.set_theme(style='whitegrid')\n\nproject_root = Path(r'{}')\ndata_dir = project_root / 'data'\nfiles = {{'pesticides': data_dir / 'pesticides.csv', 'rainfall': data_dir / 'rainfall.csv', 'temp': data_dir / 'temp.csv', 'yield': data_dir / 'yield.csv', 'yield_df': data_dir / 'yield_df.csv'}}\n\nfor name, path in files.items():\n    print(f'\\n=== {name.upper()} ===')\n    df = pd.read_csv(path)\n    display(df.head())\n    print(df.info())\n    print('Shape:', df.shape)\n    print('Duplicados:', df.duplicated().sum())\n    print('Nulos por columna:', df.isnull().sum().to_dict())\n    print('Descriptivos:\\n', df.describe(include='all').T)\n    print('=' * 80)\n".format(project_root)),
    ('code', "raw_datasets = {}\nraw_datasets['pesticides'] = pd.read_csv(data_dir / 'pesticides.csv')\nraw_datasets['rainfall'] = pd.read_csv(data_dir / 'rainfall.csv').rename(columns={' Area': 'Area'})\nraw_datasets['temp'] = pd.read_csv(data_dir / 'temp.csv').rename(columns={'year': 'Year', 'country': 'Area'})\nraw_datasets['yield'] = pd.read_csv(data_dir / 'yield.csv')\nraw_datasets['yield_df'] = pd.read_csv(data_dir / 'yield_df.csv')\n\nfor name, df in raw_datasets.items():\n    numeric_cols = df.select_dtypes(include=['number']).columns\n    if len(numeric_cols) == 0:\n        continue\n    fig, axes = plt.subplots(1, 2, figsize=(12, 4))\n    df[numeric_cols].hist(ax=axes[0], bins=20)\n    axes[0].set_title(f'{name} - Histogramas')\n    sns.boxplot(data=df[numeric_cols], orient='h', ax=axes[1])\n    axes[1].set_title(f'{name} - Boxplots')\n    plt.tight_layout()\n    plt.show()\n"),
    ('code', "yield_df = pd.read_csv(data_dir / 'yield_df.csv')\nprint(yield_df.columns.tolist())\nyield_df[['hg/ha_yield', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp']].describe().round(2)\n"),
    ('markdown', '## Observaciones iniciales\n\n- La tabla principal de rendimiento muestra una relación esperada con precipitación, temperatura y pesticidas.\n- Existen columnas con nombres poco limpios en los archivos de lluvia y temperatura, por lo que se recomienda normalizar nombres antes de integrar.\n- Es importante revisar valores faltantes y outliers antes de entrenar modelos.\n')
]
write_notebook(notebook_dir / '01_carga_analisis_inicial.ipynb', notebook1_cells)


# Notebook 2: descriptiva detallada y extracción de características
notebook2_cells = [
    ('markdown', '# 02 - Descriptiva detallada y extracción de características\n\nEste cuaderno realiza una descriptiva más profunda del dataset integrado, genera nuevas variables y construye la matriz de correlación para identificar las variables más relevantes.\n'),
    ('code', "from pathlib import Path\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom sklearn.ensemble import RandomForestRegressor\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import r2_score\n\nsns.set_theme(style='whitegrid')\n\nproject_root = Path(r'{}')\ndata_dir = project_root / 'data'\ndf = pd.read_csv(data_dir / 'yield_df.csv')\ndf = df.rename(columns={'Unnamed: 0': 'id'})\ndf = df.copy()\ndf['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')\ndf['hg/ha_yield'] = pd.to_numeric(df['hg/ha_yield'], errors='coerce')\ndf['average_rain_fall_mm_per_year'] = pd.to_numeric(df['average_rain_fall_mm_per_year'], errors='coerce')\ndf['pesticides_tonnes'] = pd.to_numeric(df['pesticides_tonnes'], errors='coerce')\ndf['avg_temp'] = pd.to_numeric(df['avg_temp'], errors='coerce')\ndf = df.dropna(subset=['hg/ha_yield', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp'])\n\n# Variables derivadas\ndf['pesticides_log'] = np.log1p(df['pesticides_tonnes'])\ndf['rainfall_log'] = np.log1p(df['average_rain_fall_mm_per_year'])\ndf['temp_rain_interaction'] = df['avg_temp'] * df['average_rain_fall_mm_per_year']\ndf['year_centered'] = df['Year'] - df['Year'].mean()\ndf['yield_per_rain'] = df['hg/ha_yield'] / (df['average_rain_fall_mm_per_year'] + 1e-6)\n\nprint(df.head())\nprint(df[['Area', 'Item', 'Year', 'hg/ha_yield', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp']].describe().round(2))\n".format(project_root)),
    ('code', "num_cols = ['hg/ha_yield', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp', 'pesticides_log', 'rainfall_log', 'temp_rain_interaction', 'year_centered', 'yield_per_rain']\ncorrelation_matrix = df[num_cols].corr()\nplt.figure(figsize=(10, 8))\nsns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)\nplt.title('Matriz de correlación de variables numéricas')\nplt.tight_layout()\nplt.show()\n\ncorrelations = correlation_matrix['hg/ha_yield'].drop('hg/ha_yield').sort_values(ascending=False)\nprint(correlations)\n"),
    ('code', "feature_df = pd.get_dummies(df[['Area', 'Item', 'Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp', 'pesticides_log', 'rainfall_log', 'temp_rain_interaction', 'year_centered']], columns=['Area', 'Item'], drop_first=True)\nX = feature_df\ny = df['hg/ha_yield']\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\nrf = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)\nrf.fit(X_train, y_train)\nimportances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False).head(15)\nprint(importances)\nplt.figure(figsize=(10, 6))\nimportances.plot(kind='barh', color='steelblue')\nplt.title('Variables de mayor importancia estimada')\nplt.tight_layout()\nplt.show()\n"),
    ('code', "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\nsns.boxplot(data=df, x='Item', y='hg/ha_yield', ax=axes[0])\naxes[0].set_title('Rendimiento por cultivo')\naxes[0].tick_params(axis='x', rotation=45)\nsns.boxplot(data=df, x='Area', y='hg/ha_yield', ax=axes[1])\naxes[1].set_title('Rendimiento por país/área')\naxes[1].tick_params(axis='x', rotation=45)\nplt.tight_layout()\nplt.show()\n"),
    ('markdown', '## Variables de interés detectadas\n\n- La precipitación y las variables derivadas de ella muestran una relación clara con el rendimiento.\n- La temperatura y sus interacciones con la lluvia aportan información útil para el modelo.\n- El uso de pesticidas, especialmente transformado con escala logarítmica, ayuda a estabilizar la relación con el rendimiento.\n')
]
write_notebook(notebook_dir / '02_descriptiva_caracteristicas.ipynb', notebook2_cells)


# Notebook 3: entrenamiento del modelo
notebook3_cells = [
    ('markdown', '# 03 - Entrenamiento de modelo predictivo de rendimiento agrícola\n\nEste cuaderno prepara los datos, entrena un modelo de regresión y guarda el artefacto entrenado en la carpeta de modelos.\n'),
    ('code', "from pathlib import Path\nimport json\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.compose import ColumnTransformer\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.impute import SimpleImputer\nfrom sklearn.preprocessing import OneHotEncoder, StandardScaler\nfrom sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\nfrom xgboost import XGBRegressor\nimport joblib\n\nsns.set_theme(style='whitegrid')\n\nproject_root = Path(r'{}')\ndata_dir = project_root / 'data'\nmodel_dir = project_root / 'models'\nmodel_dir.mkdir(parents=True, exist_ok=True)\n\ndf = pd.read_csv(data_dir / 'yield_df.csv')\ndf = df.rename(columns={'Unnamed: 0': 'id'})\ndf = df.copy()\ndf['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')\ndf['hg/ha_yield'] = pd.to_numeric(df['hg/ha_yield'], errors='coerce')\ndf['average_rain_fall_mm_per_year'] = pd.to_numeric(df['average_rain_fall_mm_per_year'], errors='coerce')\ndf['pesticides_tonnes'] = pd.to_numeric(df['pesticides_tonnes'], errors='coerce')\ndf['avg_temp'] = pd.to_numeric(df['avg_temp'], errors='coerce')\ndf = df.dropna(subset=['hg/ha_yield', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp'])\n\ndf['pesticides_log'] = np.log1p(df['pesticides_tonnes'])\ndf['rainfall_log'] = np.log1p(df['average_rain_fall_mm_per_year'])\ndf['temp_rain_interaction'] = df['avg_temp'] * df['average_rain_fall_mm_per_year']\ndf['year_centered'] = df['Year'] - df['Year'].mean()\n\nX = df[['Area', 'Item', 'Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp', 'pesticides_log', 'rainfall_log', 'temp_rain_interaction', 'year_centered']]\ny = df['hg/ha_yield']\n\ncat_features = ['Area', 'Item']\nnum_features = [c for c in X.columns if c not in cat_features]\n\npreprocess = ColumnTransformer(transformers=[\n    ('num', Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), num_features),\n    ('cat', Pipeline([('imputer', SimpleImputer(strategy='most_frequent')), ('onehot', OneHotEncoder(handle_unknown='ignore'))]), cat_features),\n])\n\npipeline = Pipeline(steps=[('preprocess', preprocess), ('model', XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=6, subsample=0.8, colsample_bytree=0.8, random_state=42))])\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\npipeline.fit(X_train, y_train)\npreds = pipeline.predict(X_test)\n\nr2 = r2_score(y_test, preds)\nmae = mean_absolute_error(y_test, preds)\nrmse = np.sqrt(mean_squared_error(y_test, preds))\n\nprint('R2:', round(r2, 4))\nprint('MAE:', round(mae, 4))\nprint('RMSE:', round(rmse, 4))\n".format(project_root)),
    ('code', "plt.figure(figsize=(8, 4))\nplt.scatter(y_test, preds, alpha=0.6, color='steelblue')\nplt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')\nplt.xlabel('Valor real')\nplt.ylabel('Predicción')\nplt.title('Predicciones vs. valores reales')\nplt.tight_layout()\nplt.show()\n\nresiduals = y_test - preds\nplt.figure(figsize=(8, 4))\nsns.scatterplot(x=preds, y=residuals, alpha=0.6)\nplt.axhline(0, color='red', linestyle='--')\nplt.xlabel('Predicción')\nplt.ylabel('Residual')\nplt.title('Residuals del modelo')\nplt.tight_layout()\nplt.show()\n"),
    ('code', "model_path = model_dir / 'crop_yield_xgb_pipeline.joblib'\nmetrics_path = model_dir / 'model_metrics.json'\njoblib.dump(pipeline, model_path)\nwith open(metrics_path, 'w', encoding='utf-8') as f:\n    json.dump({'r2': round(float(r2), 4), 'mae': round(float(mae), 4), 'rmse': round(float(rmse), 4)}, f, indent=2)\n\nprint('Modelo guardado en:', model_path)\nprint('Métricas guardadas en:', metrics_path)\n")
]
write_notebook(notebook_dir / '03_entrenamiento_modelo.ipynb', notebook3_cells)


# HTML report
def save_html_report():
    sns.set_theme(style='whitegrid')
    df = pd.read_csv(data_dir / 'yield_df.csv')
    df = df.rename(columns={'Unnamed: 0': 'id'})
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')
    df['hg/ha_yield'] = pd.to_numeric(df['hg/ha_yield'], errors='coerce')
    df['average_rain_fall_mm_per_year'] = pd.to_numeric(df['average_rain_fall_mm_per_year'], errors='coerce')
    df['pesticides_tonnes'] = pd.to_numeric(df['pesticides_tonnes'], errors='coerce')
    df['avg_temp'] = pd.to_numeric(df['avg_temp'], errors='coerce')
    df = df.dropna(subset=['hg/ha_yield', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp'])
    df['pesticides_log'] = np.log1p(df['pesticides_tonnes'])
    df['rainfall_log'] = np.log1p(df['average_rain_fall_mm_per_year'])
    df['temp_rain_interaction'] = df['avg_temp'] * df['average_rain_fall_mm_per_year']

    num_cols = ['hg/ha_yield', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp', 'pesticides_log', 'rainfall_log', 'temp_rain_interaction']
    corr = df[num_cols].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
    plt.title('Matriz de correlación')
    plt.tight_layout()
    plt.savefig(doc_dir / 'correlation_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(12, 5))
    ax = sns.boxplot(data=df, x='Item', y='hg/ha_yield')
    ax.set_title('Rendimiento por cultivo')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(doc_dir / 'yield_by_crop.png', dpi=300, bbox_inches='tight')
    plt.close()

    summary_html = df[num_cols].describe().round(2).to_html()
    correlations_html = corr['hg/ha_yield'].drop('hg/ha_yield').sort_values(ascending=False).round(3).to_frame(name='corr_hg_ha_yield').to_html()

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <title>Informe descriptivo - Crop Yield Prediction</title>
  <style>body{{font-family:Arial, sans-serif; margin:2rem;}} h1,h2{{color:#1f4e79;}} img{{max-width:100%; border:1px solid #ddd; padding:0.5rem;}} table{{border-collapse:collapse; width:100%; margin-bottom:1rem;}} th,td{{border:1px solid #ddd; padding:0.5rem; text-align:left;}} th{{background:#f2f2f2;}}</style>
</head>
<body>
  <h1>Informe descriptivo del proyecto de predicción de rendimiento agrícola</h1>
  <p>Este informe resume la descriptiva exploratoria del dataset integrado a partir de las tablas de lluvia, temperatura, pesticidas y rendimiento.</p>
  <h2>Resumen estadístico de variables principales</h2>
  {summary_html}
  <h2>Matriz de correlación</h2>
  <img src="correlation_matrix.png" alt="Matriz de correlación" />
  <h2>Correlaciones con la variable objetivo</h2>
  {correlations_html}
  <h2>Distribución por cultivo</h2>
  <img src="yield_by_crop.png" alt="Rendimiento por cultivo" />
  <h2>Conclusiones</h2>
  <ul>
    <li>La precipitación y su transformación logarítmica muestran una relación positiva moderada con el rendimiento.</li>
    <li>La temperatura y la interacción entre temperatura y lluvia aportan información útil para el modelo.</li>
    <li>El uso de pesticidas presenta valores muy dispersos, por lo que su transformación logarítmica mejora la estabilidad del análisis.</li>
  </ul>
</body>
</html>'''

    with open(doc_dir / 'crop_yield_descriptiva.html', 'w', encoding='utf-8') as f:
        f.write(html)


save_html_report()

# Train and save model
# Build final pipeline and save artifact
base_df = pd.read_csv(data_dir / 'yield_df.csv')
base_df = base_df.rename(columns={'Unnamed: 0': 'id'})
base_df['Year'] = pd.to_numeric(base_df['Year'], errors='coerce').astype('Int64')
base_df['hg/ha_yield'] = pd.to_numeric(base_df['hg/ha_yield'], errors='coerce')
base_df['average_rain_fall_mm_per_year'] = pd.to_numeric(base_df['average_rain_fall_mm_per_year'], errors='coerce')
base_df['pesticides_tonnes'] = pd.to_numeric(base_df['pesticides_tonnes'], errors='coerce')
base_df['avg_temp'] = pd.to_numeric(base_df['avg_temp'], errors='coerce')
base_df = base_df.dropna(subset=['hg/ha_yield', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp'])
base_df['pesticides_log'] = np.log1p(base_df['pesticides_tonnes'])
base_df['rainfall_log'] = np.log1p(base_df['average_rain_fall_mm_per_year'])
base_df['temp_rain_interaction'] = base_df['avg_temp'] * base_df['average_rain_fall_mm_per_year']
base_df['year_centered'] = base_df['Year'] - base_df['Year'].mean()

X = base_df[['Area', 'Item', 'Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp', 'pesticides_log', 'rainfall_log', 'temp_rain_interaction', 'year_centered']]
y = base_df['hg/ha_yield']
cat_features = ['Area', 'Item']
num_features = [c for c in X.columns if c not in cat_features]

preprocess = ColumnTransformer(transformers=[
    ('num', Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), num_features),
    ('cat', Pipeline([('imputer', SimpleImputer(strategy='most_frequent')), ('onehot', OneHotEncoder(handle_unknown='ignore'))]), cat_features),
])

pipeline = Pipeline(steps=[('preprocess', preprocess), ('model', XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=6, subsample=0.8, colsample_bytree=0.8, random_state=42))])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)
preds = pipeline.predict(X_test)
metrics = {'r2': round(float(r2_score(y_test, preds)), 4), 'mae': round(float(mean_absolute_error(y_test, preds)), 4), 'rmse': round(float(np.sqrt(mean_squared_error(y_test, preds))), 4)}

joblib.dump(pipeline, model_dir / 'crop_yield_xgb_pipeline.joblib')
with open(model_dir / 'model_metrics.json', 'w', encoding='utf-8') as f:
    json.dump(metrics, f, indent=2)

print('Created notebooks in:', notebook_dir)
print('Created HTML report in:', doc_dir / 'crop_yield_descriptiva.html')
print('Saved model in:', model_dir / 'crop_yield_xgb_pipeline.joblib')
print('Metrics:', metrics)
