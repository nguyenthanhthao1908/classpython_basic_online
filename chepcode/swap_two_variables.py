class swap:     #khoi tao class
    def __init__(self, num1, num2):         #hai thuoc tinh
        self.a = float(num1)
        self.b = float(num2)
    def myfunc(self):           #phuong thuc
        print("so a la: ", self.a)
        print("so b la: ", self.b)
        temp = self.a           #gan tam thoi
        self.a= self.b
        self.b = temp
        print("Sau khi hoan doi ta co")     #in kq
        print("so a la: ", self.a)
        print("so b la: ", self.b)
p6 = swap(6,15)
p6.myfunc()