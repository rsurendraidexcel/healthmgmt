from fastapi import FastAPI
from app.controllers.patient_controller import router as patient_router
from app.database.session import engine, Base

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include the router
app.include_router(patient_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Health Management System"}