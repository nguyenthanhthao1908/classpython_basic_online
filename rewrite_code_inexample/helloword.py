class Loichao:                  #this is class Loichao
    def __init__(self, name, age):      #hai thuoc tinh
        self.name = name
        self.age = age
    def myfunc(self):       #phuong thuc
        print("Hi everybody, I'm " + str(self.name) + str(self.age))
p1 = Loichao("Thanh Thao - ", 20)
p1.myfunc()     #truy cap den thuoc tinh
