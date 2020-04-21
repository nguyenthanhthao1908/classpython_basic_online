"""Bài 01:
    Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
"""
S1 = input("Enter a string: ")
for i in S1:
    if i == S1[0]:
        print("String received is: ", S1.replace(i, "$"))
        break