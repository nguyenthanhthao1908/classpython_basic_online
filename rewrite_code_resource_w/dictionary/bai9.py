"""Write a Python program to iterate over dictionaries using for loops."""
D = {"Name": "Thao", "Age": 20, 19: 8}
# for i in D.items():
#     print(i)

# solution 2:
for key, value in D.items():
    print(key, "is:", D[key])

