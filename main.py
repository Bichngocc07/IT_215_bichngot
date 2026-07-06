from fastapi import FastAPI
add = FastAPI()
@add.get("/")
def home():
    return {"id":1,"name":"Ngoc","age":20,"pass":True}

@add.get("/student/{student_id}")
def getStudent(student_id: int):
    for student in student:
        if (student["id"] == student_id):
            return student