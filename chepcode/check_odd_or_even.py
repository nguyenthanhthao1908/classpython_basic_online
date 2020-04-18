class check:            #khoi tao class
    def __init__(self):     #thuoc tinh
        num = int(input("enter a number: "))        #nhap so
        self.num = int(num)
    def myfunc(self):#phuong thuc
        if (self.num %2) == 0:      #chia het cho 2
            print(self.num, " Is a even number!")       #chan
        else:
            print(self.num, " Is a odd number!")        #le
p11 = check()
p11.myfunc()
