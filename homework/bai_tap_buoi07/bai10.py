"""Bài 10:
Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
"""
def check_odd(number):
   str1 = str(number)
   i = 0
   count = 0
   for i in range(len(str1)):
      if int(str1[i]) % 2 != 0:
         count += 1
   return count

print(check_odd(123456789))