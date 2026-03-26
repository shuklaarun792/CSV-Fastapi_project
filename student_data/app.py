from fastapi import FastAPI,Path
from file_load import file_load
from fastapi import HTTPException

app=FastAPI()

data=file_load()

@app.get("/")
def home():
    return "welcome to page of arun shukla"


@app.get("/student-data")
def get_all_student_data():
    return data



@app.get("/student-data/{student_id}")
def get_student_by_id(student_id: str=Path(description='Please Enter Valid Student Id',examples='STU_1001')):
    for student in data:
        if student.get("student_id") == student_id:
            return student
    
    raise HTTPException(status_code=404, detail="Student not found")
    

