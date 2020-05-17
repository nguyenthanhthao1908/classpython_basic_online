"""Bài 02: Viết chương trình thêm một chuỗi nào đó vào cuối file
"""
f2 = open('file_1_btvn_thao', 'a+', encoding='utf-8')
data = f2.write("\nClass       : Python basic online (line test Ex2)")
print(data)
f2.close()

#DONE
