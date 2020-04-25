class anonymous:            #khoi tao class anonymous 1 prama
    def __init__(self, term):       #mot thuoc tinh
        self.term= int(term)
    def myfunc(self):       #phuong thuc
        result = list(map(lambda x: 2 ** x, range(self.term)))      #dung ham an danh lambda
        print("The total terms are: ", self.term)               # so term
        for i in range(self.term):                      #i chay den term
            print("two raised to power ", i,"is", result[i])
p22=anonymous(10)
p22.myfunc()
        