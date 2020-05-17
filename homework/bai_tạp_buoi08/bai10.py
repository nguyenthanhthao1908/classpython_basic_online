"""Bài 10: Kết quả của đoạn chương trình sau là gì?"""
try:
    print("throw")
except:
    print("except")
finally:
    print("finally")

#(1): thực thi lệnh trong try -> không gặp lỗi -> in ra "throw"
#(2): không phát hiện lỗi -> bỏ qua except
#(3): tiếp tục thực hiện lệnh trong finally -> in ra "finally"