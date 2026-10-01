import pandas as pd
from sql.connection import get_engine
from analysis.visualization import visualization
import os

engine = get_engine()

def get_machine_data():
    query = """
    SELECT
        machine_id,
        COUNT(*) AS production_count,
        COUNT(*) FILTER (WHERE defect = TRUE) AS total_defects,
        AVG(cycle_time) AS avg_cycle_time,
        AVG(temperature) AS avg_temperature,
        AVG(pressure) AS avg_pressure
    FROM production
    GROUP BY machine_id
    ORDER BY machine_id;
    """

    df = pd.read_sql(query, engine)
    folder = "machine_data"
    os.makedirs(f"./images/{folder}", exist_ok=True)
    print(f"Létrejött a '{folder}' nevű mappa.")

    visualization(df["machine_id"], df["avg_cycle_time"], "Machine ID", "AVG Cycle time", "AVG Cycle time by machine", folder)
    print("Vizualizáció 1 sikeresen létrejött.")
    visualization(df["machine_id"], df["avg_temperature"], "Machine ID", "AVG Temperature", "AVG Temperature by machine", folder)
    print("Vizualizáció 2 sikeresen létrejött.")
    visualization(df["machine_id"], df["avg_pressure"], "Machine ID", "AVG Pressure", "AVG Pressure by machine", folder)
    print("Vizualizáció 3 sikeresen létrejött.")
    visualization(df["machine_id"], df["production_count"], "Machine ID", "Production count", "Production count by machine", folder)
    print("Vizualizáció 4 sikeresen létrejött.")
    visualization(df["machine_id"], df["total_defects"], "Machine ID", "Total defects", "Total defects by machine", folder)
    print("Vizualizáció 5 sikeresen létrejött.")

def overall_data():

    query = """
    SELECT
        COUNT(*) AS total_production,
        COUNT(*) FILTER (WHERE defect = TRUE) AS total_defects,
        ROUND(
            COUNT(*) FILTER (WHERE defect = TRUE) * 100.0 / COUNT(*),
            2
        ) AS defect_rate,
        ROUND(AVG(cycle_time), 2) AS avg_cycle_time,
        ROUND(AVG(temperature), 2) AS avg_temperature,
        ROUND(AVG(pressure), 2) AS avg_pressure
    FROM production;
    """
    
    df = pd.read_sql(query, engine)

    folder = "overall_data"
    os.makedirs(f"./images/{folder}", exist_ok=True)
    print(f"Létrejött a '{folder}' nevű mappa.")

    visualization(df["avg_temperature"], df["avg_cycle_time"], "AVG Temperature", "AVG Cycle time", "Temperature VS Cycle time", folder)
    print("Vizualizáció 1 sikeresen létrejött.")

def main():
    get_machine_data()
    overall_data()
    print("Összes vizualizació elkészült.")


if __name__ == "__main__":
    main()