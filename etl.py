import pandas as pd
from pathlib import Path

DATA_PATH = Path('data/raw_sales.csv')
OUTPUT_PATH = Path('data/clean_sales.csv')

def extract():
    print('extrayendo los datos...')
    df = pd.read_csv(DATA_PATH)

    return df

def transform(df):
    print('Transformando los datos...')

    # Convertir fecha
    df['date'] = pd.to_datetime(df['date'])

    # Crear columna de venta total
    df['total_sale'] = df['quantity'] * df['price']

    # Columna mes
    df['month'] = df['date'].dt.to_period('M').astype(str)

    # Agrupación por región y mes

    summary = (
        df.groupby(['region', 'month'])
        .agg(
            total_revenue=('total_sale', 'sum'),
            total_orders=('order_id', 'count'),
            total_quantity=('quantity', 'sum')
        )
        .reset_index()
    )

    return df, summary

def load(df, summary):
    print('Cargando los datos...')
    df.to_csv(OUTPUT_PATH, index=False)
    summary.to_csv('data/summary_sales.csv', index=False)

def run_etl():
    df = extract()
    df_clean, summary = transform(df)
    load(df_clean, summary)
    print('ETL concretado exitosamente')

if __name__ == '__main__':
    run_etl()

