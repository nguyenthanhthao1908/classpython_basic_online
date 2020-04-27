class table:            #khoi tao class
    def __init__(self):         #thuoc tinh
        self.num = int(input("Enter a number: "))          #nhap vao so nguyen
    def myfunc(self):       #phuong thuc
        for i in range(1, 11):      #trong khoang lon hon 1 va nho hon 11
            print(self.num, "x", i, "= ",self.num *i)
p18=table()
p18.myfunc()