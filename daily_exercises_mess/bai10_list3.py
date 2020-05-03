"""bài 3:
 Tìm những số nguyên tố trong khoảng a và b trong 1 list và in ra chỉ số index của những số đó
 """
L = [1, 3, 6, 5, 7, -9, 13, 15, 17]
a = int(input("lower:"))
b = int(input("upper:")) + 1

for num in L:
    if num > 1:
        if num in range(a, b):
            for i in range(2, num):
                if num %i == 0:
                    break
            else:
                a = L.index(num)
                print("  index", a, "- prime number:", num)