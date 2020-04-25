"""
Bài 4. Lập trình thực hiện các công việc sau:
    Nhập 3 số a, b, c bất kì
    Hãy kiểm tra xem ba số đó có phải là độ dài của các cạnh của một tam giác hay không?
    Nếu đúng là tam giác thì xác định là tam giác vuông hay không?
"""
print(" Pls enter three sides of the triangle!!!")
a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter three side: "))

condition1 = a > 0 and b > 0 and c > 0
condition2 = a + b > c > 0
condition3 = a + c > b > 0
condition4 = b + c > a > 0

if  condition1 and condition2 and condition3 and condition4:
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Omg, this is a right triangle!!!")
    else:
        print("This is sides a Triangle!!!")
else:
    print("Srrr, This is not a triangle!!!")