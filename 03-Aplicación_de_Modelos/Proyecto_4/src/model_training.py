"""
Módulo de entrenamiento de modelos para el proyecto de predicción de precios de vivienda.

Este módulo contiene funciones para entrenar, evaluar y optimizar modelos
de machine learning para la predicción de precios de viviendas.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV, cross_val_score, learning_curve
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
import xgboost as xgb
import joblib
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


def evaluate_model(y_true, y_pred, model_name="Modelo"):
    """
    Evalúa el rendimiento de un modelo de regresión.
    
    Parameters:
    -----------
    y_true : array-like
        Valores reales
    y_pred : array-like
        Valores predichos
    model_name : str
        Nombre del modelo
        
    Returns:
    --------
    dict
        Diccionario con métricas de evaluación
    """
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    metrics = {
        'model_name': model_name,
        'mse': mse,
        'rmse': rmse,
        'mae': mae,
        'r2': r2
    }
    
    print(f"=== Evaluación de {model_name} ===")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"R²: {r2:.4f}")
    print("=" * 30)
    
    return metrics


def train_model_with_cv(X_train, y_train, model, param_grid, cv=5, scoring='neg_mean_squared_error'):
    """
    Entrena un modelo con búsqueda de hiperparámetros y validación cruzada.
    
    Parameters:
    -----------
    X_train : pd.DataFrame
        Características de entrenamiento
    y_train : pd.Series
        Variable objetivo de entrenamiento
    model : sklearn estimator
        Modelo a entrenar
    param_grid : dict
        Grid de hiperparámetros
    cv : int
        Número de folds para validación cruzada
    scoring : str
        Métrica de evaluación
        
    Returns:
    --------
    tuple
        (modelo_optimizado, mejores_parámetros, mejor_puntuación)
    """
    print(f"=== Entrenando {model.__class__.__name__} con GridSearchCV ===")
    
    # GridSearchCV
    grid_search = GridSearchCV(
        model, 
        param_grid, 
        cv=cv, 
        scoring=scoring,
        n_jobs=-1,
        verbose=0
    )
    
    # Entrenar
    grid_search.fit(X_train, y_train)
    
    print(f"Mejores parámetros: {grid_search.best_params_}")
    print(f"Mejor puntuación CV: {grid_search.best_score_:.4f}")
    
    return grid_search.best_estimator_, grid_search.best_params_, grid_search.best_score_


def comprehensive_evaluation(model, X_train, X_test, y_train, y_test, cv_folds=5):
    """
    Evaluación comprehensiva de un modelo incluyendo validación cruzada.
    
    Parameters:
    -----------
    model : sklearn estimator
        Modelo entrenado
    X_train : pd.DataFrame
        Características de entrenamiento
    X_test : pd.DataFrame
        Características de prueba
    y_train : pd.Series
        Objetivo de entrenamiento
    y_test : pd.Series
        Objetivo de prueba
    cv_folds : int
        Número de folds para CV
        
    Returns:
    --------
    dict
        Diccionario con todas las métricas
    """
    model_name = model.__class__.__name__
    
    # Predicciones
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    # Evaluación en train
    train_metrics = evaluate_model(y_train, y_train_pred, f"{model_name} - Train")
    
    # Evaluación en test
    test_metrics = evaluate_model(y_test, y_test_pred, f"{model_name} - Test")
    
    # Validación cruzada
    cv_scores = cross_val_score(model, X_train, y_train, cv=cv_folds, scoring='neg_mean_squared_error')
    cv_rmse = np.sqrt(-cv_scores)
    
    print(f"=== Validación Cruzada ===")
    print(f"RMSE CV: {cv_rmse.mean():.4f} (+/- {cv_rmse.std() * 2:.4f})")
    
    # Curva de aprendizaje
    train_sizes, train_scores, val_scores = learning_curve(
        model, X_train, y_train, cv=cv_folds, 
        scoring='neg_mean_squared_error', n_jobs=-1
    )
    
    return {
        'train_metrics': train_metrics,
        'test_metrics': test_metrics,
        'cv_rmse_mean': cv_rmse.mean(),
        'cv_rmse_std': cv_rmse.std(),
        'learning_curve': (train_sizes, np.sqrt(-train_scores), np.sqrt(-val_scores))
    }


def train_linear_models(X_train, y_train, X_test, y_test):
    """
    Entrena y evalúa modelos lineales.
    
    Parameters:
    -----------
    X_train, y_train, X_test, y_test : datos de entrenamiento y prueba
        
    Returns:
    --------
    dict
        Resultados de todos los modelos lineales
    """
    print("=== Entrenando Modelos Lineales ===")
    
    # Modelos y sus grids de hiperparámetros
    models = {
        'LinearRegression': (LinearRegression(), {}),
        'Ridge': (Ridge(), {'alpha': [0.1, 1, 10, 100]}),
        'Lasso': (Lasso(), {'alpha': [0.1, 1, 10, 100]}),
        'ElasticNet': (ElasticNet(), {'alpha': [0.1, 1, 10], 'l1_ratio': [0.3, 0.5, 0.7]})
    }
    
    results = {}
    
    for name, (model, param_grid) in models.items():
        # Entrenar con optimización de hiperparámetros
        if param_grid:
            best_model, best_params, best_score = train_model_with_cv(
                X_train, y_train, model, param_grid
            )
        else:
            best_model = model.fit(X_train, y_train)
            best_params = {}
            best_score = None
        
        # Evaluación comprehensiva
        evaluation = comprehensive_evaluation(best_model, X_train, X_test, y_train, y_test)
        
        results[name] = {
            'model': best_model,
            'best_params': best_params,
            'best_cv_score': best_score,
            'evaluation': evaluation
        }
    
    return results


def train_advanced_models(X_train, y_train, X_test, y_test):
    """
    Entrena y evalúa modelos avanzados.
    
    Parameters:
    -----------
    X_train, y_train, X_test, y_test : datos de entrenamiento y prueba
        
    Returns:
    --------
    dict
        Resultados de todos los modelos avanzados
    """
    print("=== Entrenando Modelos Avanzados ===")
    
    # Modelos y sus grids de hiperparámetros
    models = {
        'RandomForest': (RandomForestRegressor(random_state=42), {
            'n_estimators': [100, 200],
            'max_depth': [10, 20, None],
            'min_samples_split': [2, 5]
        }),
        'XGBoost': (xgb.XGBRegressor(random_state=42), {
            'n_estimators': [100, 200],
            'max_depth': [3, 6, 10],
            'learning_rate': [0.01, 0.1]
        }),
        'SVR': (SVR(), {
            'kernel': ['rbf', 'linear'],
            'C': [1, 10],
            'gamma': ['scale', 'auto']
        }),
        'KNN': (KNeighborsRegressor(), {
            'n_neighbors': [3, 5, 10],
            'weights': ['uniform', 'distance'],
            'metric': ['euclidean', 'manhattan']
        })
    }
    
    results = {}
    
    for name, (model, param_grid) in models.items():
        # Entrenar con optimización de hiperparámetros
        best_model, best_params, best_score = train_model_with_cv(
            X_train, y_train, model, param_grid
        )
        
        # Evaluación comprehensiva
        evaluation = comprehensive_evaluation(best_model, X_train, X_test, y_train, y_test)
        
        results[name] = {
            'model': best_model,
            'best_params': best_params,
            'best_cv_score': best_score,
            'evaluation': evaluation
        }
    
    return results


def compare_models(all_results):
    """
    Compara todos los modelos entrenados.
    
    Parameters:
    -----------
    all_results : dict
        Resultados de todos los modelos
        
    Returns:
    --------
    pd.DataFrame
        Comparación de modelos
    """
    print("=== Comparación de Modelos ===")
    
    comparison_data = []
    
    for model_name, results in all_results.items():
        eval_data = results['evaluation']['test_metrics']
        cv_rmse = results['evaluation']['cv_rmse_mean']
        
        comparison_data.append({
            'Modelo': model_name,
            'RMSE_Test': eval_data['rmse'],
            'MAE_Test': eval_data['mae'],
            'R²_Test': eval_data['r2'],
            'RMSE_CV': cv_rmse,
            'Best_Params': str(results['best_params'])
        })
    
    comparison_df = pd.DataFrame(comparison_data)
    comparison_df = comparison_df.sort_values('RMSE_Test')
    
    print(comparison_df)
    return comparison_df


def save_model(model, filepath):
    """
    Guarda un modelo entrenado.
    
    Parameters:
    -----------
    model : sklearn estimator
        Modelo a guardar
    filepath : str
        Ruta para guardar el modelo
    """
    try:
        joblib.dump(model, filepath)
        print(f"Modelo guardado en: {filepath}")
    except Exception as e:
        print(f"Error al guardar modelo: {e}")


def load_model(filepath):
    """
    Carga un modelo guardado.
    
    Parameters:
    -----------
    filepath : str
        Ruta del modelo guardado
        
    Returns:
    --------
    sklearn estimator
        Modelo cargado o None si hay error
    """
    try:
        model = joblib.load(filepath)
        print(f"Modelo cargado desde: {filepath}")
        return model
    except Exception as e:
        print(f"Error al cargar modelo: {e}")
        return None