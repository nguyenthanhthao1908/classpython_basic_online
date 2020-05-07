"""Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String
Ví dụ:
    Input: ‘Stringings’
    Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2,  ‘n’: 2, ‘g’: 2, ‘s’: 1}
"""
S = "Stringings"
dem = {}
for i in S:
#Nếu i có trong dem, lặp lại thì tăng lên 1, chưa có thì gán = 1
    if i in dem:
        dem[i] += 1
    else:
        dem[i] = 1
print(dem)