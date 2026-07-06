from fastapi import FastAPI

app = FastAPI()

# 1. Khai báo danh sách sinh viên ban đầu (Mock Data)
students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Binh", "status": "inactive"},
    {"id": 3, "name": "Cuong", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"}
]

# 2. Định nghĩa endpoint đúng chuẩn: GET /students/active
@app.get("/students/active")
def get_active_students():
    # Sử dụng List Comprehension để duyệt và lọc sinh viên có status là "active"
    active_students = [s for s in students if s.get("status") == "active"]
    
    # 3. Bẫy dữ liệu: Xử lý trường hợp không có sinh viên nào đang học
    if not active_students:
        return {
            "message": "Không có sinh viên đang học",
            "data": []
        }
        
    # 4. Trả về kết quả mong đợi khi có dữ liệu thỏa mãn
    return {
        "message": "Danh sách sinh viên đang học",
        "data": active_students
    }