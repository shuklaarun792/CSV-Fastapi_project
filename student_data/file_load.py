import pandas as pd
from database import SessionLocal
from models import Student

def load_csv():
    df = pd.read_csv("students_complete.csv")

    # normalize columns (safe)
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    db = SessionLocal()

    for _, row in df.iterrows():
        student = Student(
            student_id=row["student_id"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            age=int(row["age"]),
            major=row["major"],
            gpa=float(row["gpa"]) if pd.notna(row["gpa"]) else None,
            attendance=float(row["attendance"]) if pd.notna(row["attendance"]) else None,
            scholarship=int(row["scholarship"]) if pd.notna(row["scholarship"]) else None,
            city=row["city"],
            status=row["status"]
        )
        db.add(student)

    db.commit()
    db.close()

load_csv()