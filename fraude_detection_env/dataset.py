from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://@localhost:5432/insurance_medical"
try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Connected to the database successfully!")
    connection.close()
except Exception as e:
    print(f"Error: {e}")