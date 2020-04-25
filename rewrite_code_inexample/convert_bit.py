class bit:
    def __init__(self):
        self.num = int(input("enter a number u want convert: "))
    def myfunc(self):
        print("Gia tri thap phan cua", self.num, "la:")
        print(bin(self.num), "- trong nhi phan")
        print(oct(self.num), "- trong he bat phan")
        print(hex(self.num), "- trong he hexa")
p24=bit()
p24.myfunc()