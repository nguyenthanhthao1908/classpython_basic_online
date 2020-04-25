class CheckYear:
    def __init__(self, year):
        self.year = float(year)
    def myfunc(self):
        if (self.year %4) == 0:
            if (self.year %100) ==0:
                if (self.year %400)==0:
                    print(int(self.year), " Is a leap year!")       #nam nhuan
                else:
                    print (int(self.year), " Is not a leap year!")
            else:
                print(int(self.year), " Is a leap year!")
        else:
            print(int(self.year), "Is not a leap year!")
p12 = CheckYear(1999)       #Ex1999
p12.myfunc()
