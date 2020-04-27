class printprime:               #khoi tao class
    def __init__(self):         #thuoc tinh
        print("enter interval [lower upper]")       #nhap so dau-cuoi
        self.lower = int(input("lower = "))
        self.upper = int(input("upper = ")) + 1
    def myfunc(self):       #phuong thuc
        for num in range (self.lower, self.upper):      #num chay trong khoang
            if num > 1:
                for i in range (2, num):
                    if (num %i)==0:
                        break
                else:
                    print(num)
p15=printprime()
p15.myfunc()