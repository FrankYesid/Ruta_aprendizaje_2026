import os
import sys

print("Iniciando script...")
try:
    import pandas as pd
    print("Pandas importado")
    import numpy as np
    print("Numpy importado")
    import joblib
    print("Joblib importado")
    from sklearn.model_selection import train_test_split
    print("Sklearn importado")
except Exception as e:
    print(f"Error al importar: {e}")
    sys.exit(1)

data_path = "data/financial_fraud_detection_dataset.csv"
if os.path.exists(data_path):
    print(f"Archivo de datos encontrado: {data_path}")
else:
    print(f"Archivo NO encontrado: {data_path}")
    sys.exit(1)

df = pd.read_csv(data_path)
print(f"Datos cargados: {df.shape}")

# ... resto del código simplificado
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

features = ['amount', 'transaction_type', 'merchant_category', 'device_used', 
            'spending_deviation_score', 'velocity_score', 'geo_anomaly_score', 'payment_channel']
target = 'is_fraud'

X = df[features]
y = df[target].astype(int)

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['amount', 'spending_deviation_score', 'velocity_score', 'geo_anomaly_score']),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['transaction_type', 'merchant_category', 'device_used', 'payment_channel'])
    ])

model = Pipeline(steps=[('pre', preprocessor), ('clf', RandomForestClassifier(n_estimators=10, random_state=42))])
print("Entrenando...")
model.fit(X, y)
print("Guardando...")
joblib.dump(model, "model/fraud_model.joblib")
print("Listo.")
