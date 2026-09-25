import pandas as pd
import glob

def extract_data(file_path):
    files = glob.glob(file_path)
    dataframes = []

    for file in files:
        df = pd.read_csv(file)
        dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)