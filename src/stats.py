import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def siniestros_por_mes(df: pd.DataFrame):
    df_2024 = df[df['dia_siniestro'].dt.year >= 2024].copy()
    df_2024['mes_anio'] = df_2024['dia_siniestro'].dt.to_period('M').astype(str)
    df_2024['mes_anio'].value_counts().sort_index().plot(kind='bar', figsize=(12,5))
    plt.title('Cantidad de siniestros por mes (desde 2024)')
    plt.ylabel('N° de siniestros')
    plt.xlabel('Mes-Año')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def distribuciones_importes(df: pd.DataFrame):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    sns.histplot(df['importe_reclamado_hojagastos'], kde=True, ax=axes[0])
    axes[0].set_title('Distribución Importe Reclamado')
    sns.histplot(df['importe_indemnizado_hojagastos'], kde=True, ax=axes[1])
    axes[1].set_title('Distribución Importe Pagado')
    plt.tight_layout()
    plt.show()

def calcular_tasa_pago(df: pd.DataFrame) -> pd.DataFrame:
    df['tasa_pago'] = df['importe_indemnizado_hojagastos'] / df['importe_reclamado_hojagastos']
    df = df.replace([float('inf'), -float('inf')], pd.NA)
    return df

def tasa_pago_por_prestacion(df: pd.DataFrame):
    top10 = df.groupby('prestacion_1_tipo_gasto')['tasa_pago'].mean().sort_values(ascending=False).head(10)
    top10.plot(kind='bar', figsize=(12, 5), color='orange')
    plt.title('Top 10 - Tasa media de pago por tipo de prestación')
    plt.ylabel('Tasa de pago')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()

def importes_promedio_por_prestacion(df: pd.DataFrame):
    top = df.groupby('prestacion_1_tipo_gasto')[['importe_reclamado_hojagastos', 'importe_indemnizado_hojagastos']].mean()
    top10 = top.sort_values(by='importe_reclamado_hojagastos', ascending=False).head(10)
    top10.plot(kind='bar', figsize=(12, 6))
    plt.title('Top 10 - Importes promedio por tipo de prestación')
    plt.ylabel('Importe')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()

def clientes_con_mas_rechazos(df: pd.DataFrame):
    df['rechazado'] = df['ace_motivo_cierre'] == 'RECHAZADO'
    top = df.groupby('nombre_cliente_gc')['rechazado'].mean().sort_values(ascending=False).head(10)
    top.plot(kind='bar', color='red', figsize=(10, 5))
    plt.title('Clientes con mayor proporción de rechazos')
    plt.ylabel('% de rechazos')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()




if __name__ == "__main__":
    from extraction import load_excel
    from transformation import clean_dataframe

    path = "data/raw/operational_raw_data_gcc_01012024_31032025.xlsx"
    df = clean_dataframe(load_excel(path))
    df = calcular_tasa_pago(df)

    tasa_pago_por_prestacion(df)
    importes_promedio_por_prestacion(df)
    clientes_con_mas_rechazos(df)
    siniestros_por_mes(df)
