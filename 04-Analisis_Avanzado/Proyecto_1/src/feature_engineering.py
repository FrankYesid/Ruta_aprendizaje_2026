import pandas as pd
import numpy as np

def process_dates(df, date_col='post_time'):
    """
    Procesa la columna de fecha y crea variables temporales.
    """
    df[date_col] = pd.to_datetime(df[date_col])
    df['hour'] = df[date_col].dt.hour
    df['month'] = df[date_col].dt.month
    df['day_of_week'] = df[date_col].dt.day_name()
    return df

def create_engagement_score(df):
    """
    Crea un score de engagement combinado.
    Engagement = likes + (comments * 2) + (shares * 3)
    """
    df['total_engagement'] = df['likes'] + (df['comments'] * 2) + (df['shares'] * 3)
    return df

def encode_categorical(df, cols=['platform', 'post_type', 'sentiment_score']):
    """
    Codifica variables categóricas.
    """
    return pd.get_dummies(df, columns=cols, drop_first=True)
