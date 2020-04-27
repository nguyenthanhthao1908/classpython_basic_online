A = [12, 5, 30, 11, 9]
i = 0
dem = 0
for i in range(0, (len(A)-1)):
    j = i + 1
    if A[i] > A[j] and i < j:
        dem += 1
print("so tap thoa man =",dem)