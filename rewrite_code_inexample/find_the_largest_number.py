class findnumber:           #khoi tao class
    def __init__(self):     #thuoc tinh
        print("enter three number:")        #nhap so
        self.a = float(input("Number a: "))
        self.b = float(input("Number b: "))
        self.c = float(input("Numbe c: "))
    def myfunc(self):       #phuong thuc
        if (self.a >= self.b) and (self.a >= self.c):       #kiem tra
            largest = self.a
        elif (self.b >= self.a) and (self.b >= self.c):
            largest = self.b
        else:
            largest = self.c
        print("The lardest number is: ", largest)
p13=findnumber()
p13.myfunc()



