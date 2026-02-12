import pandas as pd
import os

def load_engagement_data(file_path):
    """
    Carga el dataset de engagement desde un archivo CSV.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    
    df = pd.read_csv(file_path)
    # Limpiar espacios en blanco en columnas tipo object
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df

def get_data_info(df):
    """
    Retorna información básica del dataframe.
    """
    info = {
        "num_rows": df.shape[0],
        "num_cols": df.shape[1],
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict()
    }
    return info
