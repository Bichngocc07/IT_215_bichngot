from fastapi import FastAPI
from typing import List, Dict, Any

app = FastAPI()

# Danh sách dữ liệu sinh viên
students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"}
]

# 1. Đổi endpoint sang số nhiều "/students" đúng chuẩn RESTful
# 2. Sử dụng response_model để định nghĩa rõ kiểu trả về là một danh sách các Dictionary
@app.get("/students", response_model=List[Dict[str, Any]])
def get_all_students():
    """
    Hàm xử lý lấy toàn bộ danh sách sinh viên trong hệ thống.
    """
    # 3. Trả về toàn bộ danh sách thay vì chỉ phần tử đầu tiên
    return students