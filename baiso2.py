"""Bài 02:
    Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
"""
S2 = input("Enter a string: ")
m = int(input("index want delete: "))

if m < 0 or m > len(S2):
    print("index not valid!!")
else:
    print("String after delete",m,"is:", S2.replace(S2[m],""))

