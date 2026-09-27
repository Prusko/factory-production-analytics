import pandas as pd

def transform_data(df):

    duplicated_count = df.duplicated().sum()
    df = df.drop_duplicates()

    missing_count = df["pressure"].isnull().sum()
    df = df[~df["pressure"].isnull()]

    df["energy_per_product"] = round(df["energy_consuption"] / df["production_time"], 1)
    print("Calculated 'energy_per_product' column.")
    print(f"Removed duplicates: {duplicated_count}.")
    print(f"Missing values removed: {missing_count}.")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(by="timestamp")
    print("Sorted by timestamp.")
    return df