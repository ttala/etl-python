from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Airport(Base):
    __tablename__ = 'airport'

    id = Column("ID", Integer, primary_key=True)
    name = Column("Name", String)
    city = Column("City", String)
    iata = Column("IATA", String)
    date = Column("Date", String)
