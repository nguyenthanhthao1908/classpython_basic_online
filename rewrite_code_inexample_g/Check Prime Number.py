class PrimeNumber:      #khoi tao class no param
    def __init__(self):
        num=int(input("enter is a number: "))       #nhap so
        self.num = int(num)         #kieu int
    def myfunc(self):
        if self.num > 1:
            for i in range(2,self.num):
                if (self.num %i) == 0:      #khong la so nt
                    print(self.num, " Is not a prime number!")
                    print(i, "time", self.num//i, " is " , self.num)
                    break
                else:
                    print(self.num, " is a prime number!")      #so nt
        else:
            print(self.num, " is not a prime number!")
p14 = PrimeNumber()
p14.myfunc()