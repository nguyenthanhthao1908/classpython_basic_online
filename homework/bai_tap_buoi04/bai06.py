L = ['THT', '75', 'A', '1221']
dem = 0
for i in L:
    if len(i) > 1 and i[0] == i[-1]:
        dem += 1
print("So chuoi thoa man =",dem)
