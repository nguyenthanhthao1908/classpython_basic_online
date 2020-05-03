"""bài 2 : tìm tất cả những số nguyên tố nhỏ hơn 1 số x nhập vào trong 1 list """
L = [1, 3, 6, 5, 7, -9, 13, 15, 17]
x = int(input("Enter a number positive:"))
if x >= 2:
    for num in L:
        if num in range (2, x):
            for i in (2, num):
                if num %i == 0:
                    break
                else:
                    print(num)
else:
    print("___Enter again!!!!___")