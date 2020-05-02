"""
Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

D1 = {1:10, 2:20}
D2 = {3:30, 4:40}
D3 = {5:50,6:60}
D = dict()          #tao dict rong, cach 2:D={}
for i in (D1, D2, D3):
    D.update(i)
print(D)
