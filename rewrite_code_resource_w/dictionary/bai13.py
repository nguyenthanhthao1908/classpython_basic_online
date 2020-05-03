"""Write a Python program to map two lists into a dictionary."""

Key = ["Name", "Age", 19]
Value = ["Thao", 20, 8]

D = dict(zip(Key, Value))   #zip: return a iterator of dataset tuple
print(D)
