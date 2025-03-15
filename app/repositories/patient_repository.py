from sqlalchemy.orm import Session
from app.models.patient import Patient

class PatientRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_patient(self, patient_id: int) -> Patient:
        return self.db.query(Patient).filter(Patient.id == patient_id).first()

    def get_patients(self, skip: int = 0, limit: int = 100) -> list[Patient]:
        return self.db.query(Patient).offset(skip).limit(limit).all()

    def create_patient(self, patient: Patient) -> Patient:
        self.db.add(patient)
        self.db.commit()
        self.db.refresh(patient)
        return patient

    def update_patient(self, patient_id: int, patient_data: dict) -> Patient:
        patient = self.db.query(Patient).filter(Patient.id == patient_id).first()
        if patient:
            for key, value in patient_data.items():
                setattr(patient, key, value)
            self.db.commit()
            self.db.refresh(patient)
        return patient

    def delete_patient(self, patient_id: int) -> Patient:
        patient = self.db.query(Patient).filter(Patient.id == patient_id).first()
        if patient:
            self.db.delete(patient)
            self.db.commit()
        return patient