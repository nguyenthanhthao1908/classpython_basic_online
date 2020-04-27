import math         #truy cap den math
class sqrt:     #khoi tao ham
    def __init__(self,num):     #thuoc tinh
        self.num=num
    def myfunc(self):       #phuong thuc
        print("the square root of " + str(self.num) + " is " + str(math.sqrt(self.num)))
p3 = sqrt(36)
p3.myfunc()     #truy cap thuoc tinh