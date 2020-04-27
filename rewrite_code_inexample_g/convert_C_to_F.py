class conver:       #khoi tao class
    def __init__(self, celsius):        #mot thuoc tinh
        self.celsius = float(celsius)
    def myfunc(self):           #phuong thuc
        fahrenheit = ((self.celsius * 1.8) + 32)        #chuyen doi
        print(self.celsius, "do C = ", fahrenheit, "do F")
p9=conver(37.5)
p9.myfunc()
