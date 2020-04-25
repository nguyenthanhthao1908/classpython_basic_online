class Addnumbers:                       #khoi tao lop
    def __init__(self, num1, num2):     #thuoc tinh
        self.num1 = num1
        self.num2= num2
    def myfunc(self):               #phuong thuc
        sum = self.num1 + self.num2
        print(str(self.num1) + " + " + str(self.num2) + " = " + str(sum))       #
p2 = Addnumbers(2, 3)           #example 2,3
p2.myfunc()
