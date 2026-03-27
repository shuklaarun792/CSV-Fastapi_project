from sqlalchemy import Column, Integer, String, Float
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    
    student_id = Column(String(50), unique=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    age = Column(Integer)
    major = Column(String(100))
    gpa = Column(Float)
    attendance = Column(Float)
    scholarship = Column(Integer)
    city = Column(String(100))
    status = Column(String(50))