import random           #truy cap random
class RandomNumber:         #khoi tao class
    def __init__(self, start, to):          #thuoc tinh
        self.start = start
        self.to = to
    def myfunc(self):           #phuong thuc
        print("so may man la: ", random.randint(self.start,self.to))     #dung random de lua chon
p7=RandomNumber(5,15)
p7.myfunc()
