class ascii:        #khoi tao class 1 parameres
    def __init__(self):         #thuoc tinh
        self.symbol = input("enter a symbol: ")
    def myfunc(self):       #phuong thuc
        if type(self.symbol) is str:        #neu symbol la str
            print("The ASII value of ", self.symbol, "is", ord(self.symbol))     #su dung ord de chuyen doi
        else:
            if type(self.symbol) is int:        #neu symbol la int
                print("The ASII value of ", self.symbol, "is", chr(self.symbol))  # su dung chr de chuyen doi
p25=ascii()
p25.myfunc()