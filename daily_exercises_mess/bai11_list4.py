"""bài 4:
Tính giá trị trung bình của những số nguyên tố trong 1 list .
(nếu trong list k có số nguyên tố trả về -1 , 1 list phải có ít nhất 10 giá trị)
"""
import statistics
L1 = [1, 3, 6, 5, 7, -9, 13, 15, 17, 55, 47]
L2 = []
for num in L1:
    if num > 1:
        for i in range(2, num):
            if num %i == 0:
                break
        else:
            L2.append(num)
            a = statistics.mean(L2)
            print("average:", a)
