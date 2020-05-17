"""Bài 05: Viết hàm
        def count_upper_lower(str)
trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str"""
def count_upper_lower(str):
    D = {'upper': 0, 'lower': 0}
    for i in str:
        if i.isupper():     #đếm ký tự viết hoa
            D['upper'] += 1
        elif i.islower():   #đếm ký tự viết thường
            D['lower'] += 1
    print('str:', str)
    print("Number uppercase:", D['upper'])
    print("Number lowercase:", D['lower'])
print(count_upper_lower('Nguyễn Thị Thanh Thảo'))