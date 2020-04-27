class sochiahet:            #khoi tao class
    def __init__(self,num):     #1thuoc tinh
        self.num = int(num)
    def myfunc(self):       #phuong thuc
        my_list = [12,65,54,39,102,339,221]
        listnum= list(filter(lambda x: (x % self.num == 0), my_list))       #dung lambda de loc
        print("cac so chia het cho", self.num,"la:", listnum)
p23= sochiahet(13)
p23.myfunc()
