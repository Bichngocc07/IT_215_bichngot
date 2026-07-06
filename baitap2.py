from fastapi import FastAPI
from typing import List, Dict, Any

app = FastAPI()

students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"}
]


@app.get("/students", response_model=List[Dict[str, Any]])
def get_all_students():
    """
    Hàm xử lý lấy toàn bộ danh sách sinh viên trong hệ thống.
    """
    return students
