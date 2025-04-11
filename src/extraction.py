import pandas as pd


def load_excel(path: str) -> pd.DataFrame:
    """
    Carga un archivo Excel y devuelve un DataFrame
    """
    xls = pd.ExcelFile(path)
    df = pd.read_excel(xls)
    return df


def initial_overview(df: pd.DataFrame):
    """
    Muestra información inicial del DataFrame
    """
    print("Primeras filas:")
    print(df.head())
    print("\nÚltimas filas:")
    print(df.tail())
    print("\nShape:", df.shape)
    print("\nDtypes:")
    print(df.dtypes)
    print("\nColumnas:")
    print(df.columns)


if __name__ == "__main__":
    path = "data/raw/operational_raw_data_gcc_01012024_31032025.xlsx"
    df = load_excel(path)
    initial_overview(df)