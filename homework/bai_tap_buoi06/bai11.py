"""Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
Ví dụ:
    Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    Output: {'item1': 1150, 'item2': 300}
    """

L = [{'item': 'item1', 'amount': 400},
     {'item': 'item2', 'amount': 300},
     {'item': 'item1', 'amount': 750}]
D = {L[0]['item'] : L[0]['amount']}
for i in L:
     if i['item'] in D:       #'item' trong D, lặp lại thì update lên, chưa thì gán
          D[i['item']] += i['amount']
     else:
          D[i['item']] = i['amount']
print(D)


# Solution 2:
#Counter dùng để đếm các hastable
# from collections import Counter
# L = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# new_dict = Counter()
# for i in L:
#     new_dict[i['item']] += i['amount']
# print(new_dict)
