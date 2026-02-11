# Proyecto 4: Predicción del Precio de Vivienda - Módulos SRC

## 📁 Estructura de la carpeta src

La carpeta `src` contiene los módulos de Python reutilizables para el proyecto:

### 📋 Archivos principales:

1. **`__init__.py`** - Archivo de inicialización del paquete
2. **`data_preprocessing.py`** - Módulo de preprocesamiento de datos
3. **`feature_engineering.py`** - Módulo de ingeniería de características
4. **`model_training.py`** - Módulo de entrenamiento de modelos

---

## 🔧 Módulo: data_preprocessing.py

### Funciones principales:

#### `load_data(file_path)`
Carga el dataset de Boston Housing desde archivo CSV.
```python
df = load_data('../data/BostonHousing.csv')
```

#### `validate_data(df)`
Valida la calidad del dataset y retorna información de validación.
```python
validation_info = validate_data(df)
```

#### `clean_data(df)`
Limpia el dataset removiendo duplicados y valores atípicos.
```python
df_clean = clean_data(df)
```

#### `scale_features(X_train, X_test, method='robust')`
Escala las características numéricas (opciones: 'robust', 'standard', 'minmax').
```python
X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test, method='robust')
```

#### `prepare_data(df, target_column='MEDV', test_size=0.2, random_state=42, scale_method='robust')`
Prepara el dataset completo para modelado.
```python
components = prepare_data(df, target_column='MEDV', test_size=0.2)
```

#### `save_preprocessing_components(components, save_path)`
Guarda los componentes de preprocesamiento.
```python
save_preprocessing_components(components, '../models/preprocessing_components.pkl')
```

#### `load_preprocessing_components(load_path)`
Carga componentes de preprocesamiento guardados.
```python
components = load_preprocessing_components('../models/preprocessing_components.pkl')
```

---

## 🛠️ Módulo: feature_engineering.py

### Funciones principales:

#### `create_interaction_features(df)`
Crea características de interacción entre variables.
```python
df_interactions = create_interaction_features(df)
```

#### `create_polynomial_features(df, degree=2)`
Crea características polinómicas.
```python
df_polynomial = create_polynomial_features(df, degree=2)
```

#### `create_ratio_features(df)`
Crea características de ratio (cocientes).
```python
df_ratios = create_ratio_features(df)
```

#### `create_binning_features(df, n_bins=5)`
Crea características de binning/discretización.
```python
df_binned = create_binning_features(df, n_bins=5)
```

#### `select_features_univariate(X, y, k=20, score_func='f_regression')`
Selecciona mejores características usando pruebas univariadas.
```python
X_selected, selected_features, scores = select_features_univariate(X, y, k=20)
```

#### `select_features_importance(X, y, n_estimators=100, top_n=20)`
Selecciona características basadas en importancia de Random Forest.
```python
X_selected, selected_features, importance_df = select_features_importance(X, y)
```

#### `engineer_all_features(df, target_column='MEDV')`
Aplica toda la ingeniería de características en un solo paso.
```python
df_engineered = engineer_all_features(df, target_column='MEDV')
```

---

## 🤖 Módulo: model_training.py

### Funciones principales:

#### `evaluate_model(y_true, y_pred, model_name)`
Evalúa el rendimiento de un modelo de regresión.
```python
metrics = evaluate_model(y_test, y_pred, "Random Forest")
```

#### `train_model_with_cv(X_train, y_train, model, param_grid)`
Entrena modelo con búsqueda de hiperparámetros y validación cruzada.
```python
best_model, best_params, best_score = train_model_with_cv(X_train, y_train, model, param_grid)
```

#### `comprehensive_evaluation(model, X_train, X_test, y_train, y_test)`
Evaluación comprehensiva incluyendo validación cruzada y curvas de aprendizaje.
```python
evaluation_results = comprehensive_evaluation(model, X_train, X_test, y_train, y_test)
```

#### `train_linear_models(X_train, y_train, X_test, y_test)`
Entrena y evalúa modelos lineales (Linear, Ridge, Lasso, ElasticNet).
```python
linear_results = train_linear_models(X_train, y_train, X_test, y_test)
```

#### `train_advanced_models(X_train, y_train, X_test, y_test)`
Entrena y evalúa modelos avanzados (Random Forest, XGBoost, SVR, KNN).
```python
advanced_results = train_advanced_models(X_train, y_train, X_test, y_test)
```

#### `compare_models(all_results)`
Compara todos los modelos entrenados.
```python
comparison_df = compare_models(all_results)
```

#### `save_model(model, filepath)`
Guarda un modelo entrenado.
```python
save_model(best_model, '../models/random_forest_model.pkl')
```

#### `load_model(filepath)`
Carga un modelo guardado.
```python
model = load_model('../models/random_forest_model.pkl')
```

---

## 📖 Ejemplos de uso

### Flujo completo de trabajo:

```python
# Importar módulos
import sys
sys.path.append('../src')
from data_preprocessing import load_data, prepare_data
from feature_engineering import engineer_all_features
from model_training import train_linear_models, train_advanced_models, compare_models

# 1. Cargar y preparar datos
df = load_data('../data/BostonHousing.csv')
components = prepare_data(df)

# 2. Ingeniería de características
df_engineered = engineer_all_features(components['X_train'])

# 3. Entrenar modelos
linear_results = train_linear_models(df_engineered, components['y_train'], 
                                   df_engineered, components['y_test'])

advanced_results = train_advanced_models(df_engineered, components['y_train'], 
                                        df_engineered, components['y_test'])

# 4. Comparar modelos
all_results = {**linear_results, **advanced_results}
comparison = compare_models(all_results)
```

---

## 📋 Dependencias

Los módulos requieren las siguientes librerías:

```python
# Librerías básicas
pandas
numpy

# Preprocesamiento
scikit-learn

# Modelos avanzados
xgboost

# Visualización (opcional)
matplotlib
seaborn

# Guardado de modelos
joblib
```

---

## 🎯 Notas importantes

1. **Reutilización**: Todos los módulos están diseñados para ser reutilizables
2. **Documentación**: Cada función incluye docstrings detallados
3. **Validación**: Las funciones incluyen validación de errores y advertencias
4. **Consistencia**: Los nombres de funciones y parámetros siguen estándares consistentes
5. **Rendimiento**: Optimizadas para datasets medianos (como Boston Housing)