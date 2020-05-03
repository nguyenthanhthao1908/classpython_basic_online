"""Write a Python program to get a dictionary from an object's fields"""
class Dict():
    def __init__(self):
        self.name = 'Thao'
        self.age = 20
        self.classs = 1404
    def my_function(self):
        pass
D = Dict()
print(D.__dict__)