from fastapi import FastAPI
from typing import List

app = FastAPI()

# Giả lập cơ sở dữ liệu danh sách sinh viên
students = ["An", "Binh", "Cuong"]

# 1. Đổi endpoint sang danh từ số nhiều theo chuẩn RESTful
# 2. Sử dụng response_model để tường minh kiểu dữ liệu trả về (Mảng các string)
@app.get("/students", response_model=List[str])
def get_students():
    # 3. Trả về trực tiếp Python list. 
    # FastAPI sẽ tự động ép kiểu (serialize) thành một JSON Array chuẩn: ["An", "Binh", "Cuong"]
    return students