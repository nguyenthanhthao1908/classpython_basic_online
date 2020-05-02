"""
Write a Python script to check whether a given key already exists in a dictionary.
"""
D = {'Name': 'Thao', 'Age': 20, 1: 10, 2: 20}
def key(x):
    if x in D:
        print("Key is present in the dict!")
    else:
        print("Key NOT is present in dict!!!")
dapan = key(1)