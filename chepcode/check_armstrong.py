class armstrong:
    def __init__(self):
        self.num = int(input("enter a number: "))
    def myfunc(self):
        sum = 0
        a = self.num
        while a > 0:
            digit = a % 10
            sum += digit ** 3
            a //= 10
        if a == sum:
            print(a, " Is an armstrong number")
        else:
            print(a, "Is not an armstrong number")

p19 = armstrong()
p19.myfunc()