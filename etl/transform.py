
def transform_data(df):
    original_count = len(df)
    
    df = df.drop_duplicates()
    duplicated_count = original_count - len(df)

    df = df[~df["pressure"].isnull()]
    missing_count = (original_count - duplicated_count) - len(df)

    df["energy_per_product"] = round(df["energy_consuption"] / df["production_time"], 1)
    print("Calculated 'energy_per_product' column.")
    print(f"Removed duplicates: {duplicated_count}.")
    print(f"Missing values removed: {missing_count}.")
    return df