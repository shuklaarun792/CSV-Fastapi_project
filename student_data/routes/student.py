from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def home():
    return {"message": "Welcome To My FastAPI"}

# ✅ 1. Get all students (unchanged)
@router.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


# 🔥 2. Filter API (NEW ROUTE)
@router.get("/students/filter")
def filter_students(
    age_gt: int = Query(None),
    city: str = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Student)

    if age_gt is not None:
        query = query.filter(models.Student.age > age_gt)

    if city:
        query = query.filter(models.Student.city == city)

    return query.all()


# 🔹 Get student by ID
@router.get("/students/{student_id}")
def get_student(
    student_id: str = Path(
        description="Enter Valid Student Id",
        examples={"example": {"value": "STU_1000"}}
    ),
    db: Session = Depends(get_db)
):
    student = db.query(models.Student).filter(
        models.Student.student_id == student_id
    ).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student