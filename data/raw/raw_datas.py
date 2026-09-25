#This python file will create the raw datas with random values
import pandas as pd
import numpy as np


defect_types = ["WELDING", "PRESSURE", "CRACK", "LOOSE"]


for day in range(1, 32):
    rows = []
    
    for i in range(1, 5):
        invalid_id = np.random.randint(0, 250, 10)
        for j in range(250):
            defect = np.random.randint(0, 101) > 90
            defect_type = ""
            time = round(np.random.uniform(40, 70), 1)
            if (defect): 
                defect_type = defect_types[np.random.randint(0,4)]
            
            rows.append({
                "timestamp": f"2026-09-{day}",
                "line_id": f"0{i}",
                "machine_id": f"M0{i}",
                "product_id": f"P{j}",
                "cycle_time": time,
                "temperature": round(np.random.uniform(70, 90), 1),
                "pressure": round(np.random.uniform(2, 6), 1),
                "production_time": time,
                "defect": defect,
                "defect_type": defect_type,
                "energy_consuption": round(np.random.uniform(10, 30), 1)
            })

        for id in invalid_id:
            if not rows[id]["defect"]:
                rows[id]["pressure"]= np.nan

        duplicate_count = np.random.randint(5,15)
        duplicate_id = np.random.choice(len(rows), duplicate_count, replace=False)
        for id in duplicate_id:
            rows.append(rows[id].copy())
    
    df = pd.DataFrame(rows)
    df.to_csv(f"products_09-{day}.csv", index=False)
    print(f"products_09-{day}.csv created.")
    print("Rows: ", len(rows))
    print("Duplicates: ", df.duplicated().sum())

print("All raw datas csv succesfully created!")