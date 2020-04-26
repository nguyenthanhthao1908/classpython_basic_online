#tim giai thua cua mot so

def factorial(n):           #ham factoeial
    if n == 0:              #n=0 thi tra ve 1
        return 1
    else:
        return n*factorial(n-1)
n = int(input("input a number to computer the factorial: "))
print(factorial(n))