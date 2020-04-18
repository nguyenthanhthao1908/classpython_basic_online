class fibonacci:            #khoi tao class 1 thuoc tinh
    def __init__(self,num):         #thuoc tinh
        self.num = int(num)
    def myfunc(self):       #phuong thuc
        n1, n2 = 0, 1
        count = 0
        if self.num < 0:        #nhap lai so +
            print("enter a positive integer!")
        elif self == 1:
            print("Fibonacci sequence upto ",self.num, ": ")
            print(n1)
        else:
            print("Fibonacci sequence: ")
            while count < self.num:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count +=1
p18=fibonacci(7)
p18.myfunc()