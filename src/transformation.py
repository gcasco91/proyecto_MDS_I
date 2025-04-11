import pandas as pd
import numpy as np

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica transformaciones y limpieza al DataFrame:
    - Convierte fechas
    - Elimina registros negativos
    - Filtra año 2024
    - Filtra casos inconsistentes
    - Elimina CUSTOMER_SERVICE en dm
    - Elimina outliers usando método IQR
    """
    
    # Normalizar nombres de columnas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[áéíóúñ]", lambda m: {
            "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ñ": "n"
        }[m.group()], regex=True)
    )

    # Conversión de fechas
    date_cols = ['fecha_apertura', 'dia_siniestro']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], format="%d/%m/%Y", errors="coerce")

    # Eliminar importes negativos
    df = df[(df['importe_reclamado_hojagastos'] >= 0) & (df['importe_indemnizado_hojagastos'] >= 0)]

    # Filtrar registros inconsistentes
    df = df[~((df['op_estado'] == 'Abierto') & (df['ace_estado'] == 'Cerrado'))]

    # Eliminar registros de atención al cliente
    df = df[df['dm'] != 'CUSTOMER_SERVICE']

    # Eliminar outliers usando método IQR en importe reclamado
    Q1 = df['importe_reclamado_hojagastos'].quantile(0.25)
    Q3 = df['importe_reclamado_hojagastos'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df['importe_reclamado_hojagastos'] >= lower_bound) & (df['importe_reclamado_hojagastos'] <= upper_bound)]

    # Eliminar outliers usando método IQR en importe indemnizado
    Q1 = df['importe_indemnizado_hojagastos'].quantile(0.25)
    Q3 = df['importe_indemnizado_hojagastos'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df['importe_indemnizado_hojagastos'] >= lower_bound) & (df['importe_indemnizado_hojagastos'] <= upper_bound)]

    # Filtrar siniestros desde 2023
    df = df[df['dia_siniestro'].dt.year >= 2023].copy()

    return df

def export_clean_data(df: pd.DataFrame, output_path: str):
    """Guarda el DataFrame limpio a CSV"""
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    path = "data/raw/operational_raw_data_gcc_01012024_31032025.xlsx"
    out = "data/processed/clean_data.csv"
    from extraction import load_excel
    df = load_excel(path)
    df_clean = clean_dataframe(df)
    export_clean_data(df_clean, out)