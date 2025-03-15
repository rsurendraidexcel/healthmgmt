from sqlalchemy import Column, Integer, String, Date
from app.database.session import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    address = Column(String)
    phone_number = Column(String)
    date_of_birth = Column(Date)