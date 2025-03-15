from fastapi import APIRouter, Depends, HTTPException
from app.services.patient_service import PatientService
from app.database.session import get_db
from app.schemas.patient import Patient, PatientCreate
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/patients/", response_model=Patient)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    service = PatientService(db)
    db_patient = service.create_patient(patient)
    return db_patient

@router.get("/patients/{patient_id}", response_model=Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    service = PatientService(db)
    db_patient = service.get_patient(patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@router.get("/patients/", response_model=list[Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = PatientService(db)
    return service.get_patients(skip, limit)

@router.put("/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, patient: PatientCreate, db: Session = Depends(get_db)):
    service = PatientService(db)
    updated_patient = service.update_patient(patient_id, patient)
    if updated_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated_patient

@router.delete("/patients/{patient_id}", response_model=Patient)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    service = PatientService(db)
    deleted_patient = service.delete_patient(patient_id)
    if deleted_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return deleted_patient