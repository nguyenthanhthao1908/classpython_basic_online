"""Write a Python program to remove a key from a dictionary."""

D = {"Class": 1404, "Age": 20, 19: 8}
i = input("enter element del:")
if i in D:
    del D[i]
print(D)