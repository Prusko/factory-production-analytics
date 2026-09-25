from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def main():
    print("Starting ETL processing...")

    input_file_path = "./data/raw/products_09-*.csv"
    output_file_path = "./data/processed/clean_products.csv"
    
    df = extract_data(input_file_path)
    print(f"Extracted {len(df)} rows.")

    df = transform_data(df)
    print(f"After transformation {len(df)} rows.")

    load_data(df, output_file_path)



if __name__ == "__main__":
    main()