import pandas as pd
from sql.connection import get_engine

def load_production():

    engine = get_engine()

    df = pd.read_csv("./data/processed/clean_products.csv")
    df.drop(columns=["production_id"], errors="ignore", inplace=True)
    print(df.head())

    df.to_sql("production", engine, if_exists="append", index=False)

    print(f"Loaded {len(df)} rows into production.")

if __name__ == "__main__":
    load_production()