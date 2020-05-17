"""
Bài 07: Đoạn chương trình sau in ra gì?"""

number = 5.0
try:
    r = 10/number
    print(r)
except:
    print("Oops! Error occurred.")

# (1): thực thi khối lệnh trong try
# (2): không có lỗi -> bỏ qua except
# (3): in ra kết quả r=2.0
