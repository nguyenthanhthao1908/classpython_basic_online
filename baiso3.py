"""
Bài 3. Lập chương trình thực hiện các công việc sau:
    Nhập 1 số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
    Tính tổng các chữ số của số đó.
    Hiển thị kết qủa ra màn hình
"""

n = int(input("enter random number <1000, n ="))
while True:
    if n > 0 and n < 1000:
        print("Number entered  correct!!!!")
        a = n // 100
        b = (n - 100 * a) // 10
        c = (n - 100 * a - 10 * b)
        sum = a + b + c
        print("Sum numbers entered is:",sum)
        break

    else:
        print("Number entered not correct, Please enter again!!!!")
        break


