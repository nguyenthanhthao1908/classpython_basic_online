"""bài 1 : tìm tất cả những số nguyên tố trong 1 list """
L = [1, 2, 3, 5, -7, 9, 11, 13, 14]
for num in L:
    if num > 1:
        for i in (2, num):
            if num %i == 0:
                break
            print(num, end=' ')