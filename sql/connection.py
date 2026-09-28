from sqlalchemy import create_engine

def get_engine():
    return create_engine(
        "postgresql+psycopg2://postgres:600969@localhost:5432/smart_factory"
    )