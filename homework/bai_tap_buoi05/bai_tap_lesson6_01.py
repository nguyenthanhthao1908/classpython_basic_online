""" Các phương thức của Set"""

S1 = {3, 19, 8, 99, 'thanh', 'thao', (23, 't'), 6.7}
S2 = {'t', 99, 68, 'e', 'thanh', 3}

# S1.add('ThanhThaoNguyenhThaoNguyen')     #{3, 99, 6.7, 8, 'thanh', 19, 'thao', (23, 't'), 'ThanhThaoNguyen'}
# S1.clear()                       #set()
# S3 = S1.copy()                   #{3, 99, 6.7, 8, 19, (23, 't'), 'thanh', 'thao'}
# S1.difference(S2)                #{6.7, 'thao', 8, (23, 't'), 19}
# S1.difference_update(S2)         #{6.7, 8, (23, 't'), 19, 'thao'}
# S1.discard(3)                    # {'thao', 99, 'thanh', 6.7, 8, 19, (23, 't')}
# S1.intersection(S2)              #->{'thanh', 3, 99}
# S1.intersection_update(S2)       #S1 = {3, 99, 'thanh'}
# print(S1.isdisjoint(S2))         #False
# print(S1.issubset(S2))           #False
# print(S1.issuperset(S2))         #False
# print(S1.pop())                  #element random
# S1.remove(3)                     #{'thanh', 99, 6.7, (23, 't'), 8, 'thao', 19}
# print(S1.symmetric_difference(S2))     #{68, 'e', 6.7, 8, 19, 'thao', (23, 't'), 't'}
# S1.symmetric_difference_update(S2)     #S1= {68, 6.7, 't', 8, 19, 'thao', (23, 't'), 'e'}
# print(S1.union(S2))                    #{3, 99, 'e', 6.7, 68, 8, 'thao', 'thanh', 19, 't', (23, 't')}
S1.update(S2)                    #S1={3, 99, 68, 6.7, 8, (23, 't'), 't', 'e', 'thao', 19, 'thanh'}

print(S1)

