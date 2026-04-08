import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import os

# Configuración
base_path = r"d:\GitHub\Ruta_aprendizaje_2024\06-Integración_con_el_Mundo_Real\Proyecto_1"
data_path = os.path.join(base_path, "data", "financial_fraud_detection_dataset.csv")
model_path = os.path.join(base_path, "model", "fraud_model.joblib")

# Carga de datos
df = pd.read_csv(data_path)

# Selección de características
features = ['amount', 'transaction_type', 'merchant_category', 'device_used', 
            'spending_deviation_score', 'velocity_score', 'geo_anomaly_score', 'payment_channel']
target = 'is_fraud'

X = df[features]
y = df[target].astype(int)

# Preprocesamiento
numeric_features = ['amount', 'spending_deviation_score', 'velocity_score', 'geo_anomaly_score']
categorical_features = ['transaction_type', 'merchant_category', 'device_used', 'payment_channel']

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Pipeline completo
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=50, random_state=42, class_weight='balanced'))
])

# Entrenamiento rápido (puedes ajustar n_estimators)
print("Entrenando modelo...")
model_pipeline.fit(X, y)

# Guardar
os.makedirs(os.path.dirname(model_path), exist_ok=True)
joblib.dump(model_pipeline, model_path)
print(f"Modelo guardado en: {model_path}")
