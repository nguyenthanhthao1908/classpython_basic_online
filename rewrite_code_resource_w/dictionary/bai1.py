"""Viết tập lệnh Python để sắp xếp (tăng dần và giảm dần) một dict theo giá trị"""
import operator
D = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_1 = dict(sorted(D.items()))    #sx theo tăng dan theo key
print(sorted_1)

sorted_2 = dict(sorted(D.items(),key=operator.itemgetter(1)))   #sx tang theo gtri
print(sorted_2)

sorted_3 = dict(sorted(D.items(), key=operator.itemgetter(1), reverse=True)) #giam theo gtri
print(sorted_3)


