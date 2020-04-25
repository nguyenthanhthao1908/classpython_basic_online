import cmath  #import thu vien math
class AreaOfTriangle:           #khoi tao class area of triangla
    def __init__(self):
        print("enter the three sidess of the triangle: ")       #nhap do dai
        self.a = float(input("enter first side: "))
        self.b = float(input("enter second side: "))
        self.c = float(input("enter three side: "))
    def conditionOfaTriangle(self):                             #kiem tra dieu kien tao thanh tam giac
        condition1 = self.a > 0 and self.b >0 and self.c > 0
        condition2 = self.a + self.b > self.c > 0
        condition3 = self.a + self.c > self.b > 0
        condition4 = self.b + self.c > self.a > 0
        if condition1 and condition2 and condition3 and condition4:
            p = (self.a + self.b + self.c) / 2          #chu vi
            Area = (cmath.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c)))     #dien tich
            print("Area of triangle is " + str(Area))
        else:
            print("This is not a Triangel!!! ")
p4 = AreaOfTriangle()
p4.conditionOfaTriangle()