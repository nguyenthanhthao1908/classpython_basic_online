"""Bài 06: Viết hàm
        def is_pangram(str, alphabet)
đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần"""
def is_pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in str.lower():
            return False
    return True
print(is_pangram("the quick brown fox jumps over the lazy dog"))
print(is_pangram('nguyen thi thanh thao'))

#Solution 2:
# - dùng mã ASCII: bảng chứ cái thường pangram từ 96 - 122.
