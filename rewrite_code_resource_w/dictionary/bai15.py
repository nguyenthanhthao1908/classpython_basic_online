"""Write a Python program to get the maximum and minimum value in a dictionary. """

D = {3: 30, 2: 20, 19: 8}

print("Maximum:", max(D.keys(), key=(lambda k: D[k])))
print("Minimum:", min(D.keys(), key=(lambda k: D[k])))