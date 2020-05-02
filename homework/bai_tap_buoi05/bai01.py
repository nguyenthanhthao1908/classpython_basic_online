L1 = ['t', 4, 8, 'app', '3.12', 56, 88]      #list
T1 = (1, 'Hi', 'Night!', 2.718, 1+3j)        #tuple

L2 = list(T1)
T2 = tuple(L1)

print(type(L2))
print(type(T2))
