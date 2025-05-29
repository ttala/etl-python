import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import pandas as pd

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)


df = pd.read_csv('_airport.csv')
airport = [
    Airport(Name=row['Airport Name'], City=row['City'], IATAe=row['IATA'], Date=row['Exported date'])
    for _, row in df.iterrows()
]

# Bulk insert
session.add_all(airports)
session.commit()
session.close()