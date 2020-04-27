L02 = [45, 7, 9, 4, 6, 88, 332, 1, 4, 6]
Min, Max = L02[0], L02[0]
for i in L02:
    if Min > i:
        Min = i
    elif Max < i:
        Max = i
print("Min =",Min)
print("Max =",Max)