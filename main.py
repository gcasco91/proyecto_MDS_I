import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


from extraction import load_excel, initial_overview
from transformation import clean_dataframe, export_clean_data
from stats import (
    calcular_tasa_pago,
    distribuciones_importes,
    tasa_pago_por_prestacion,
    importes_promedio_por_prestacion,
    clientes_con_mas_rechazos,
    siniestros_por_mes
)

RAW_PATH = "C:/Users/gcasc/proyectos/proyecto_MDS_I/data/raw/operational_raw_data_gcc_01012024_31032025.xlsx"
CLEAN_PATH = "C:/Users/gcasc/proyectos/proyecto_MDS_I/data/processed/clean_data.csv"

if __name__ == "__main__":
    print("\n🔄 Extrayendo datos...")
    df = load_excel(RAW_PATH)
    initial_overview(df)

    print("\n🧹 Transformando datos...")
    df_clean = clean_dataframe(df)
    export_clean_data(df_clean, CLEAN_PATH)

    print("\n📊 Ejecutando análisis estadístico...")
    df_clean = calcular_tasa_pago(df_clean)
    tasa_pago_por_prestacion(df_clean)
    importes_promedio_por_prestacion(df_clean)
    clientes_con_mas_rechazos(df_clean)
    siniestros_por_mes(df_clean)

    print("\n✅ Proyecto ejecutado con éxito.")