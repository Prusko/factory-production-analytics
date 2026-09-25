import pandas as pd

def load_data(df, output):
    df.to_csv(output, index=False)
    print("Data loaded successfully")