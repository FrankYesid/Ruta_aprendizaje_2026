"""
Módulo de preprocesamiento de datos para el proyecto de predicción de precios de vivienda.

Este módulo contiene funciones para cargar, limpiar, validar y preparar datos
de viviendas de Boston para modelos de machine learning.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split
import joblib
import warnings
warnings.filterwarnings('ignore')


def load_data(file_path):
    """
    Carga el dataset de Boston Housing desde un archivo CSV.
    
    Parameters:
    -----------
    file_path : str
        Ruta al archivo CSV
        
    Returns:
    --------
    pd.DataFrame
        Dataset cargado o None si hay error
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset cargado exitosamente: {df.shape}")
        print(f"Columnas: {list(df.columns)}")
        return df
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None


def validate_data(df):
    """
    Valida la calidad del dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset a validar
        
    Returns:
    --------
    dict
        Diccionario con información de validación
    """
    validation_info = {
        'shape': df.shape,
        'missing_values': df.isnull().sum().to_dict(),
        'duplicated_rows': df.duplicated().sum(),
        'data_types': df.dtypes.to_dict(),
        'numeric_columns': df.select_dtypes(include=[np.number]).columns.tolist(),
        'categorical_columns': df.select_dtypes(include=['object']).columns.tolist()
    }
    
    print("=== Información de Validación ===")
    print(f"Dimensiones: {validation_info['shape']}")
    print(f"Filas duplicadas: {validation_info['duplicated_rows']}")
    
    if validation_info['missing_values']:
        missing_total = sum(validation_info['missing_values'].values())
        print(f"Valores faltantes totales: {missing_total}")
    
    return validation_info


def clean_data(df):
    """
    Limpia el dataset removiendo duplicados y valores atípicos.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset a limpiar
        
    Returns:
    --------
    pd.DataFrame
        Dataset limpio
    """
    print("=== Limpieza de Datos ===")
    original_shape = df.shape
    
    # Remover duplicados
    df_clean = df.drop_duplicates()
    print(f"Duplicados removidos: {original_shape[0] - df_clean.shape[0]}")
    
    # Detectar y remover outliers extremos usando IQR
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 3 * IQR
        upper_bound = Q3 + 3 * IQR
        
        outliers = df_clean[(df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)]
        if len(outliers) > 0:
            print(f"Outliers detectados en {col}: {len(outliers)}")
            df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]
    
    print(f"Datos finales después de limpieza: {df_clean.shape}")
    return df_clean


def scale_features(X_train, X_test, method='robust'):
    """
    Escala las características numéricas.
    
    Parameters:
    -----------
    X_train : pd.DataFrame
        Datos de entrenamiento
    X_test : pd.DataFrame
        Datos de prueba
    method : str
        Método de escalado: 'standard', 'minmax', 'robust'
        
    Returns:
    --------
    tuple
        (X_train_scaled, X_test_scaled, scaler)
    """
    print(f"=== Escalado con {method} ===")
    
    # Seleccionar escalador
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    elif method == 'robust':
        scaler = RobustScaler()
    else:
        raise ValueError("Método debe ser 'standard', 'minmax' o 'robust'")
    
    # Ajustar y transformar
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train),
        columns=X_train.columns,
        index=X_train.index
    )
    
    X_test_scaled = pd.DataFrame(
        scaler.transform(X_test),
        columns=X_test.columns,
        index=X_test.index
    )
    
    print(f"Características escaladas: {X_train_scaled.shape[1]}")
    return X_train_scaled, X_test_scaled, scaler


def prepare_data(df, target_column='MEDV', test_size=0.2, random_state=42, scale_method='robust'):
    """
    Prepara el dataset completo para modelado.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset completo
    target_column : str
        Nombre de la columna objetivo
    test_size : float
        Proporción del set de prueba
    random_state : int
        Semilla para reproducibilidad
    scale_method : str
        Método de escalado
        
    Returns:
    --------
    dict
        Diccionario con todos los componentes preparados
    """
    print("=== Preparación Completa de Datos ===")
    
    # Separar características y objetivo
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # División train-test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    print(f"Train: {X_train.shape}, Test: {X_test.shape}")
    
    # Escalado
    X_train_scaled, X_test_scaled, scaler = scale_features(
        X_train, X_test, method=scale_method
    )
    
    # Guardar componentes
    components = {
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test,
        'X_train_scaled': X_train_scaled,
        'X_test_scaled': X_test_scaled,
        'scaler': scaler,
        'feature_names': X.columns.tolist(),
        'target_name': target_column
    }
    
    return components


def save_preprocessing_components(components, save_path='../models/preprocessing_components.pkl'):
    """
    Guarda los componentes de preprocesamiento.
    
    Parameters:
    -----------
    components : dict
        Diccionario con componentes a guardar
    save_path : str
        Ruta para guardar
    """
    try:
        joblib.dump(components, save_path)
        print(f"Componentes guardados en: {save_path}")
    except Exception as e:
        print(f"Error al guardar componentes: {e}")


def load_preprocessing_components(load_path='../models/preprocessing_components.pkl'):
    """
    Carga los componentes de preprocesamiento.
    
    Parameters:
    -----------
    load_path : str
        Ruta del archivo a cargar
        
    Returns:
    --------
    dict
        Componentes cargados o None si hay error
    """
    try:
        components = joblib.load(load_path)
        print(f"Componentes cargados desde: {load_path}")
        return components
    except Exception as e:
        print(f"Error al cargar componentes: {e}")
        return None


def create_sample_data(n_samples=100):
    """
    Crea datos de ejemplo para pruebas.
    
    Parameters:
    -----------
    n_samples : int
        Número de muestras a generar
        
    Returns:
    --------
    pd.DataFrame
        Dataset de ejemplo
    """
    np.random.seed(42)
    
    data = {
        'CRIM': np.random.normal(3.6, 8.6, n_samples),
        'ZN': np.random.choice([0, 12.5, 25, 50, 100], n_samples),
        'INDUS': np.random.normal(11.1, 6.9, n_samples),
        'CHAS': np.random.choice([0, 1], n_samples, p=[0.93, 0.07]),
        'NOX': np.random.normal(0.55, 0.12, n_samples),
        'RM': np.random.normal(6.3, 0.7, n_samples),
        'AGE': np.random.normal(68.6, 28.1, n_samples),
        'DIS': np.random.normal(3.8, 2.1, n_samples),
        'RAD': np.random.choice(range(1, 25), n_samples),
        'TAX': np.random.choice([187, 279, 330, 666], n_samples),
        'PTRATIO': np.random.normal(18.5, 2.2, n_samples),
        'B': np.random.normal(356, 92, n_samples),
        'LSTAT': np.random.normal(12.7, 7.1, n_samples),
        'MEDV': np.random.normal(22.5, 9.2, n_samples)
    }
    
    return pd.DataFrame(data)