from app.repositories.patient_repository import PatientRepository
from app.schemas.patient import PatientCreate
from app.models.patient import Patient

class PatientService:
    def __init__(self, db):
        self.repository = PatientRepository(db)

    def get_patient(self, patient_id: int) -> Patient:
        return self.repository.get_patient(patient_id)

    def get_patients(self, skip: int = 0, limit: int = 100) -> list[Patient]:
        return self.repository.get_patients(skip, limit)

    def create_patient(self, patient: PatientCreate) -> Patient:
        db_patient = Patient(**patient.model_dump())
        return self.repository.create_patient(db_patient)

    def update_patient(self, patient_id: int, patient: PatientCreate) -> Patient:
        db_patient = self.repository.get_patient(patient_id)
        if db_patient:
            for key, value in patient.model_dump().items():
                setattr(db_patient, key, value)
            self.repository.db.commit()
            self.repository.db.refresh(db_patient)
        return db_patient

    def delete_patient(self, patient_id: int) -> Patient:
        return self.repository.delete_patient(patient_id)