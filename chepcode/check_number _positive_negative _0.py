class check:        #khoi tao lop
    def __init__(self, num):        #thuoc tinh
        self.num = float(num)
    def myfunc(self):       #phuong thuc
        if self.num > 0:        #in so +
            print("This is positive number ")
        elif self.num == 0: # laf so 0
            print("This is zero")
        else:           #in ra so -
            print("This is negative number ")

p10 = check(20)
p10.myfunc()    #truy cap thuoc tinh
