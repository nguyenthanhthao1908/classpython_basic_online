class sum:          #khoi tao class sum
    def __init__(self, num):        #thuoc tinh
        self.num = num
    def myfunc(self):                #phuong thuc
        if self.num < 0:             #nhap lai mot so +
            print("enter a positive number")
        else:
            sum = 0                     #tong ban dau =0
            while (self.num > 0 ):      #lap
                sum += self.num         #cong roi gan
                self.num -= 1           #tru 1 roi gan
            print("The sum is ", sum)
p20=sum(16)             #vidu cho 16
p20.myfunc()