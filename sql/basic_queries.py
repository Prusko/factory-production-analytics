from sqlalchemy import text
from sql.connection import get_engine

engine = get_engine()

query = text("""
    SELECT * 
    FROM production
    LIMIT 10;
""")

with engine.connect() as connection:
    result = connection.execute(query)

    for row in result:
        print(row)