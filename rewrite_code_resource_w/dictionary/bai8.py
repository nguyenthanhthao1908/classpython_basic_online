"""Write a Python script to merge two Python dictionaries"""
D1 = {"Name": "Thao", "Age": 20}
D2 = {"Class": "python", "Methods": "only"}

D = D1.copy()
D.update(D2)
print(D)