""" Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""
D = {0: 10, 1: 20}
D.update({2: 30})
print(D)