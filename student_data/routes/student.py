from fastapi import APIRouter, Depends, HTTPException,Path
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter()

# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def home():
    return {"message": "FastAPI with MySQL"}
# 🔹 Get all students
@router.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

# 🔹 Get student by ID
@router.get("/students/{student_id}")
def get_student(student_id: str=Path(description="Enter Valid Student Id",example="STU_1000"), db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.student_id == student_id
    ).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student