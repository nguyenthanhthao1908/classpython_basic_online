import math     #tru cap den math
class quadration:       #khoi tao
    def __init__(self):         #thuoc tinh
        print("Input a,b,c for quadration equations ax^2 + bx +c =0")       #nhap he so
        self.a = float(input())
        self.b = float(input())
        self.c = float(input())
    def SloveEquation(self):        #phuong thuc
        if  self.a==0 :     #kiem tra dk
            print("This is not quadratic equation!")
        else:
            delta = (self.b)**2 - 4*self.a*self.b
            if delta > 0:   #hai nghiem phan biet
                print("First Solution is: ", ((- self.b + math.sqrt(delta)) / 2*self.a))
                print("Second Solution is: ", ((-self.b - math.sqrt(delta)) / 2*self.a))
            elif delta == 0:    #nghiem kep
                print("the equations has solution is: ", -self.b / (2*self.a))
            else:       #vo nghiem
                print("equation no solution!!!")
p5=quadration()
p5.SloveEquation()

