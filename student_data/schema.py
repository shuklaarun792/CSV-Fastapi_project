from pydantic import BaseModel

class StudentBase(BaseModel):
    student_id: str
    name: str
    age: int
    gpa: float

class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True