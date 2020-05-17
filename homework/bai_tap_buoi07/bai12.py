"""Bài 12:
 Viết hàm: def find_x(a_list, x)
 trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
 """
def find_x(a_list, x):
    index = []
    for i in range(len(a_list)):
        if x == a_list[i]:
            index.append(i)
    if len(index) == 0:
        return -1
    return index
print(find_x([3, 45, 3, 5, 45, 3, 6],3))