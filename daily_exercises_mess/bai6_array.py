#loai bo cac phan tu trung lap trong list
a = [10,20,30,20,10,50,60,40,80,50,40]   #list a

dup_items = set()               #tao set rong
uniq_items = []                 #tao list rong
for x in a:                     #x chay trong list a
    # Neu x khong co trong set, tiep tuc thuc hien
    if x not in dup_items:
        uniq_items.append(x)        #them phan tu vao cuoi list
        dup_items.add(x)            #them phan tu vao set

print(dup_items)