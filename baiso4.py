"""Bài 04:
    Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào,
    nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
"""
S4 = input("Enter a string:")
if len(S4) < 2:
    print("String received = empty. Pls enter string len > 2!!!")
elif len(S4) == 2:
    print("String received is:", S4[0:2])
else:
    print("String received is:", S4[0:2] + S4[-2:])