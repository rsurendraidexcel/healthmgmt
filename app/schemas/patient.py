from pydantic import BaseModel
from datetime import date

# Base schema for creating a patient
class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    address: str
    phone_number: str
    date_of_birth: date

# Schema for reading/returning a patient
class Patient(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    address: str
    phone_number: str
    date_of_birth: date

    class Config:
        from_attributes = True  # Enables ORM mode (previously `orm_mode = True`)