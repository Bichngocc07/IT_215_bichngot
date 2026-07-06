from fastapi import FastAPI
from typing import List

app = FastAPI()

students = ["An", "Binh", "Cuong"]


@app.get("/students", response_model=List[str])
def get_students():

    return students
