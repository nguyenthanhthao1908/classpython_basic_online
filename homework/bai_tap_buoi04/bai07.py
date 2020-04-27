A = [12, 47, 9, 2, 4, 6, 8, 3]
B = [12, 2, 1, 99, 4, 6, 3]
test = False
for i in A:
    for j in B:
        if i == j:
            test = True
            print('phan tu chung la:',j)