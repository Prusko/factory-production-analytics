from sqlalchemy import text
from sql.connection import get_engine

engine = get_engine()

query = text("""
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
""")

with engine.connect() as connection:
    result = connection.execute(query)

    for row in result:
        print(row)