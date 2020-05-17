"""Bài 04: Viết hàm
        def get_file_size(file)
    để lấy và trả về dung lượng của file"""
import os
def getSize(file_name):
    st = os.stat(file_name)     #stat: stat tren file_name
    return st.st_size       #st_size: kich co cua file(byte)
print(getSize('file_2_btvn_thao'))