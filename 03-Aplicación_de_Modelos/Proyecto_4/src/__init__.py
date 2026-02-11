"""
Paquete de utilidades para el proyecto de predicción de precios de vivienda.

Este paquete contiene módulos para:
- Preprocesamiento de datos (data_preprocessing)
- Ingeniería de características (feature_engineering)  
- Entrenamiento de modelos (model_training)
"""

from .data_preprocessing import (
    load_data,
    validate_data,
    clean_data,
    scale_features,
    prepare_data,
    save_preprocessing_components,
    load_preprocessing_components,
    create_sample_data
)

from .feature_engineering import (
    create_interaction_features,
    create_polynomial_features,
    create_ratio_features,
    create_binning_features,
    select_features_univariate,
    select_features_importance,
    engineer_all_features
)

from .model_training import (
    evaluate_model,
    train_model_with_cv,
    comprehensive_evaluation,
    train_linear_models,
    train_advanced_models,
    compare_models,
    save_model,
    load_model
)

__version__ = "1.0.0"
__author__ = "Proyecto de Predicción de Precios de Vivienda"

__all__ = [
    # Data Preprocessing
    'load_data',
    'validate_data', 
    'clean_data',
    'scale_features',
    'prepare_data',
    'save_preprocessing_components',
    'load_preprocessing_components',
    'create_sample_data',
    
    # Feature Engineering
    'create_interaction_features',
    'create_polynomial_features',
    'create_ratio_features',
    'create_binning_features',
    'select_features_univariate',
    'select_features_importance',
    'engineer_all_features',
    
    # Model Training
    'evaluate_model',
    'train_model_with_cv',
    'comprehensive_evaluation',
    'train_linear_models',
    'train_advanced_models',
    'compare_models',
    'save_model',
    'load_model'
]