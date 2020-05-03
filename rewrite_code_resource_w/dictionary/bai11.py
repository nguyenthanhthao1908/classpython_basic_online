"""Write a Python program to multiply all the items in a dictionary."""

D = {"Class": 1404, "Age": 20, 19: 8}
P = 1
for i in D:
    P *= D[i]
print("Result:", P)