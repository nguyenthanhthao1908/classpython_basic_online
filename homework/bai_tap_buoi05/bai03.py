L = ['Thanh', 1999, 'A', ('Thanh Thao', 19, 'N',99), 30]
dem = 0
for i in L:
    if isinstance(i, tuple):  #Hàm isinstance dùng để kiểm tra một phần tử có thuộc một class nào đó không
        break
    dem += 1
print(dem)