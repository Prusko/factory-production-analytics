import pandas as pd
import glob

files = glob.glob("../data/raw/2026-09*.csv")

for file in files:
    print(file)