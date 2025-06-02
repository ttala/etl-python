import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Airport
import pandas as pd
from scraper import scrp_data

DATABASE_URL = os.getenv("DATABASE_URL")

def init():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create tables
    Base.metadata.create_all(engine)
    return session

def insert_all(session, data):
    session.add_all(airports)
    session.commit()
    session.close()

if __name__ == "__main__":
    scrp_data()
    df = pd.read_csv('_airports.csv')
    airports = [
        Airport(name=row['Airport Name'], city=row['City'], iata=row['IATA'], date=row['Exported date'])
        for _, row in df.iterrows()
    ]
# Bulk insert
    session = init()
    insert_all(session, airports)
