class findfactor:
    def __init__(self):
        self.num = int(input("enter a integer: "))
        factorial = 1
    def myfunc(self):
        factorial = 1
        if self.num < 0:
             print("Factorial does not exist for negative numbers")
        elif self.num == 0:
             print("The factorial of 0 = 1")
        else:
             for i in range (1, self.num + 1):
                 factorial = factorial * i
                 print("The factorial of ", self.num, "= ", factorial)
p16=findfactor()
p16.myfunc()