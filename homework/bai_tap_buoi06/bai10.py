"""
Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
"""
S = "Hello!! My name is: Nguyen Thi Thanh Thao Thao"
tach_word = S.split(" ")    #split: dấu hiệu phân tách
dem = {}
for i in tach_word:       #tương tự giống bai9
    if i in dem:
        dem[i] += 1
    else:
        dem[i] = 1
print(dem)