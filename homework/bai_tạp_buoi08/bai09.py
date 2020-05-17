"""Bài 09: Kết quả output của đoạn chương trình sau là gì?"""
def hoan_function():
    try:
        print('Monday')
    finally:
        print('Sunday')
hoan_function()

#(1): hàm thực thi lệnh trong try -> in ra 'Monday'
#(2): gặp lệnh finally (luôn được thực thi) -> in ra 'Sunday'