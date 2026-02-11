"""
Módulo de ingeniería de características para el proyecto de predicción de precios de vivienda.

Este módulo contiene funciones para crear nuevas características, seleccionar
las más relevantes y optimizar el conjunto de datos para modelos de machine learning.
"""

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings('ignore')


def create_interaction_features(df):
    """
    Crea características de interacción entre variables numéricas.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset original
        
    Returns:
    --------
    pd.DataFrame
        Dataset con características de interacción
    """
    print("=== Creando Características de Interacción ===")
    
    df_interactions = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    # Interacciones clave para precios de vivienda
    if 'RM' in numeric_cols and 'LSTAT' in numeric_cols:
        df_interactions['RM_LSTAT'] = df['RM'] * df['LSTAT']
    
    if 'RM' in numeric_cols and 'CRIM' in numeric_cols:
        df_interactions['RM_CRIM'] = df['RM'] * df['CRIM']
    
    if 'DIS' in numeric_cols and 'NOX' in numeric_cols:
        df_interactions['DIS_NOX'] = df['DIS'] * df['NOX']
    
    if 'AGE' in numeric_cols and 'INDUS' in numeric_cols:
        df_interactions['AGE_INDUS'] = df['AGE'] * df['INDUS']
    
    if 'TAX' in numeric_cols and 'PTRATIO' in numeric_cols:
        df_interactions['TAX_PTRATIO'] = df['TAX'] * df['PTRATIO']
    
    print(f"Características de interacción creadas: {df_interactions.shape[1] - df.shape[1]}")
    return df_interactions


def create_polynomial_features(df, degree=2, include_bias=False):
    """
    Crea características polinómicas para variables seleccionadas.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset original
    degree : int
        Grado máximo del polinomio
    include_bias : bool
        Si incluir término de sesgo
        
    Returns:
    --------
    pd.DataFrame
        Dataset con características polinómicas
    """
    print("=== Creando Características Polinómicas ===")
    
    # Variables candidatas para transformación polinómica
    poly_candidates = ['RM', 'LSTAT', 'CRIM', 'DIS', 'NOX']
    available_candidates = [col for col in poly_candidates if col in df.columns]
    
    if not available_candidates:
        print("No hay variables candidatas para transformación polinómica")
        return df
    
    # Crear características polinómicas
    poly = PolynomialFeatures(degree=degree, include_bias=include_bias)
    poly_features = poly.fit_transform(df[available_candidates])
    
    # Crear nombres para las nuevas características
    feature_names = poly.get_feature_names_out(available_candidates)
    
    # Crear DataFrame con características polinómicas
    poly_df = pd.DataFrame(
        poly_features, 
        columns=feature_names,
        index=df.index
    )
    
    # Combinar con el dataset original (excluyendo las originales para evitar duplicados)
    df_poly = pd.concat([
        df.drop(columns=available_candidates),
        poly_df
    ], axis=1)
    
    print(f"Características polinómicas creadas: {df_poly.shape[1] - df.shape[1]}")
    return df_poly


def create_ratio_features(df):
    """
    Crea características de ratio (cocientes) entre variables.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset original
        
    Returns:
    --------
    pd.DataFrame
        Dataset con características de ratio
    """
    print("=== Creando Características de Ratio ===")
    
    df_ratios = df.copy()
    
    # Ratios relevantes para precios de vivienda
    if 'RM' in df.columns and 'LSTAT' in df.columns:
        # Ratio habitaciones vs estatus de bajos ingresos
        df_ratios['RM_LSTAT_RATIO'] = df['RM'] / (df['LSTAT'] + 1)
    
    if 'TAX' in df.columns and 'CRIM' in df.columns:
        # Ratio impuestos vs criminalidad
        df_ratios['TAX_CRIM_RATIO'] = df['TAX'] / (df['CRIM'] + 0.1)
    
    if 'DIS' in df.columns and 'NOX' in df.columns:
        # Ratio distancia vs concentración de óxidos
        df_ratios['DIS_NOX_RATIO'] = df['DIS'] / (df['NOX'] + 0.01)
    
    if 'AGE' in df.columns and 'INDUS' in df.columns:
        # Ratio edad vs industrialización
        df_ratios['AGE_INDUS_RATIO'] = df['AGE'] / (df['INDUS'] + 1)
    
    if 'B' in df.columns and 'PTRATIO' in df.columns:
        # Ratio población negra vs ratio profesor-alumno
        df_ratios['B_PTRATIO_RATIO'] = df['B'] / (df['PTRATIO'] + 1)
    
    # Reemplazar infinitos con valores máximos razonables
    for col in df_ratios.columns:
        if 'RATIO' in col:
            df_ratios[col] = df_ratios[col].replace([np.inf, -np.inf], np.nan)
            df_ratios[col] = df_ratios[col].fillna(df_ratios[col].median())
    
    print(f"Características de ratio creadas: {df_ratios.shape[1] - df.shape[1]}")
    return df_ratios


def create_binning_features(df, n_bins=5):
    """
    Crea características de binning (discretización) para variables continuas.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset original
    n_bins : int
        Número de bins para discretización
        
    Returns:
    --------
    pd.DataFrame
        Dataset con características de binning
    """
    print("=== Creando Características de Binning ===")
    
    df_binned = df.copy()
    
    # Variables candidatas para binning
    bin_candidates = ['LSTAT', 'CRIM', 'DIS', 'AGE', 'TAX']
    
    for col in bin_candidates:
        if col in df.columns:
            # Crear bins con quantiles
            binned_col = f"{col}_BINNED"
            df_binned[binned_col] = pd.qcut(
                df[col], 
                q=n_bins, 
                labels=[f'Q{i+1}' for i in range(n_bins)],
                duplicates='drop'
            )
            
            # También crear versión numérica de los bins
            binned_num_col = f"{col}_BINNED_NUM"
            df_binned[binned_num_col] = pd.qcut(
                df[col], 
                q=n_bins, 
                duplicates='drop'
            ).cat.codes
    
    print(f"Características de binning creadas: {df_binned.shape[1] - df.shape[1]}")
    return df_binned


def select_features_univariate(X, y, k=20, score_func='f_regression'):
    """
    Selecciona las mejores características usando pruebas univariadas.
    
    Parameters:
    -----------
    X : pd.DataFrame
        Características
    y : pd.Series
        Variable objetivo
    k : int
        Número de características a seleccionar
    score_func : str
        Función de puntuación: 'f_regression' o 'mutual_info_regression'
        
    Returns:
    --------
    tuple
        (X_selected, selected_features, scores)
    """
    print(f"=== Selección Univariada ({score_func}) ===")
    
    # Seleccionar función de puntuación
    if score_func == 'f_regression':
        scorer = f_regression
    elif score_func == 'mutual_info_regression':
        scorer = mutual_info_regression
    else:
        raise ValueError("score_func debe ser 'f_regression' o 'mutual_info_regression'")
    
    # Aplicar selección
    selector = SelectKBest(score_func=scorer, k=k)
    X_selected = selector.fit_transform(X, y)
    
    # Obtener características seleccionadas
    selected_features = X.columns[selector.get_support()]
    
    # Obtener puntuaciones
    scores = selector.scores_
    feature_scores = pd.DataFrame({
        'feature': X.columns,
        'score': scores,
        'selected': selector.get_support()
    }).sort_values('score', ascending=False)
    
    # Crear DataFrame con características seleccionadas
    X_selected_df = pd.DataFrame(X_selected, columns=selected_features, index=X.index)
    
    print(f"Características seleccionadas: {len(selected_features)}")
    print(f"Mejores 10 características:")
    print(feature_scores.head(10))
    
    return X_selected_df, selected_features, feature_scores


def select_features_importance(X, y, n_estimators=100, top_n=20):
    """
    Selecciona características basadas en importancia de Random Forest.
    
    Parameters:
    -----------
    X : pd.DataFrame
        Características
    y : pd.Series
        Variable objetivo
    n_estimators : int
        Número de árboles en Random Forest
    top_n : int
        Número de características principales a seleccionar
        
    Returns:
    --------
    tuple
        (X_selected, selected_features, importance_df)
    """
    print("=== Selección por Importancia (Random Forest) ===")
    
    # Entrenar Random Forest
    rf = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
    rf.fit(X, y)
    
    # Obtener importancias
    importances = rf.feature_importances_
    
    # Crear DataFrame de importancias
    importance_df = pd.DataFrame({
        'feature': X.columns,
        'importance': importances
    }).sort_values('importance', ascending=False)
    
    # Seleccionar top_n características
    selected_features = importance_df.head(top_n)['feature'].values
    
    # Crear DataFrame con características seleccionadas
    X_selected = X[selected_features]
    
    print(f"Características seleccionadas: {len(selected_features)}")
    print(f"Mejores 10 características:")
    print(importance_df.head(10))
    
    return X_selected, selected_features, importance_df


def engineer_all_features(df, target_column='MEDV'):
    """
    Aplica toda la ingeniería de características al dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset original
    target_column : str
        Nombre de la columna objetivo
        
    Returns:
    --------
    pd.DataFrame
        Dataset con todas las características ingenierizadas
    """
    print("=== Aplicando Ingeniería de Características ===")
    
    # Separar objetivo si existe
    if target_column in df.columns:
        X = df.drop(columns=[target_column])
        y = df[target_column]
    else:
        X = df.copy()
        y = None
    
    # 1. Interacciones
    X_interactions = create_interaction_features(X)
    
    # 2. Características polinómicas
    X_polynomial = create_polynomial_features(X_interactions)
    
    # 3. Ratios
    X_ratios = create_ratio_features(X_polynomial)
    
    # 4. Binning
    X_binned = create_binning_features(X_ratios)
    
    # Recombinar con objetivo si existe
    if y is not None:
        final_df = pd.concat([X_binned, y], axis=1)
    else:
        final_df = X_binned
    
    print(f"Características finales: {final_df.shape[1]} (original: {df.shape[1]})")
    
    return final_df