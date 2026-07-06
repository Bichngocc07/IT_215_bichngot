from fastapi import FastAPI

app = FastAPI()

# 1. Khai báo danh sách sách ban đầu (Mock Data) bao gồm các trường hợp lỗi dữ liệu
books = [
    {"id": 1, "title": "Python Basics", "quantity": 10},
    {"id": 2, "title": "FastAPI Beginner", "quantity": 2},
    {"id": 3, "title": "Clean Code", "quantity": 5},
    {"id": 4, "title": "Database Design", "quantity": 0},
    {"id": 5, "title": "Web Dev Design", "quantity": 50},
    {"id": 6, "title": "Java Basics"},               # Bẫy dữ liệu: Thiếu quantity
    {"id": 7, "title": "Spring Boot", "quantity": -2} # Bẫy dữ liệu: Quantity âm
]

# 2. Tạo endpoint theo đúng yêu cầu: GET /books/low-stock
@app.get("/books/low-stock")
def get_low_stock_books():
    low_stock_books = []
    
    # Duyệt danh sách sách bằng vòng lặp for theo giải pháp đã chọn
    for book in books:
        # Bẫy dữ liệu 1: Bỏ qua nếu bị thiếu trường quantity
        if "quantity" not in book:
            continue
            
        # Bẫy dữ liệu 2: Bỏ qua nếu quantity âm (dữ liệu không hợp lệ)
        if book["quantity"] < 0:
            continue
            
        # Quy tắc nghiệp vụ: Lọc các sách có quantity <= 5
        if book["quantity"] <= 5:
            low_stock_books.append(book)
            
    # Ràng buộc đầu ra: Xử lý trường hợp không có sách nào sắp hết hàng
    if not low_stock_books:
        return {
            "message": "Không có sách nào sắp hết hàng",
            "data": []
        }
        
    # Kết quả trả về mong đợi
    return {
        "message": "Danh sách sách sắp hết hàng",
        "data": low_stock_books
    }