class Convert:          #khoi tao claaa
    def __init__(self, km):         #thuoc tinh
        self.km = float(km)
    def myfunc(self):               #phuong thuc
        conv_fac = 0.621371
        Miles = self.km * conv_fac
        print(self.km, "km = ", Miles, "miles")
p8=Convert(7)
p8.myfunc()