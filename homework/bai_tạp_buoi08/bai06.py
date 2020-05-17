"""Bài 06:
Viết chương trình tạp ra 26 file text có tên lần lượt từ A.txt, B.txt đến Z.txt
"""
import string, os
if not os.path.exists("letters"):      #os.path.exists: kiem tra 1 thư mục có tồn tại hay không
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

