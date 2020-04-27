A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
dem = A.count(0)
for i in A:
    if A.count(i) > 1:
        del A[i]
print(A)
print("Length A =", len(A))


