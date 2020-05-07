"""Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
        Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict"""

D1 = {
    'dict1': [10, 'th', 78, [58, 4], 45, 'Nguyen'],
    'dict2': [20, 'a', 't', 200, 65, 'Thanh'],
    'dict3': [30, 40, 59,'hi', 68, 'Thao']
    }
D2 = D1['dict1'][-1] + D1['dict2'][-1] + D1['dict3'][-1]
print(D2)