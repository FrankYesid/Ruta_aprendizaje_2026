import matplotlib.pyplot as plt
import seaborn as sns

def plot_engagement_by_platform(df):
    """
    Grafica el engagement promedio por plataforma.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x='platform', y='likes', data=df, estimator='mean')
    plt.title('Likes promedio por Plataforma')
    plt.show()

def plot_engagement_correlation(df):
    """
    Grafica la matriz de correlación de las métricas numéricas.
    """
    numeric_df = df.select_dtypes(include=[np.number])
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Matriz de Correlación de Métricas')
    plt.show()

def plot_sentiment_impact(df):
    """
    Visualiza el impacto del sentimiento en el engagement.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='sentiment_score', y='likes', data=df)
    plt.title('Impacto del Sentimiento en los Likes')
    plt.show()
