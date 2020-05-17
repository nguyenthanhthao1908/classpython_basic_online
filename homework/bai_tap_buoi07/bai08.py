"""Bài 08: - Viết hàm: def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
    - Viết hàm: def bmi_information(m, h)
    để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
"""
class BMI:
    def __init__(self):
        self.m = float(input("enter weight (kg):"))
        self.h = float(input("enter high(meters):"))
        self.g = int(input("enter gender (boy enter 1 - girl enter 2): "))
        self.bmi = round(self.m / (self.h ** 2))     #round: lam tron
    def body_mass_index(self):
        print("Your BMI is:", self.bmi)
    def bmi_information(self):
        if self.g == 1:
            if self.bmi < 20:
                print("too thinnnnnn, Pls eat!!!!")
            if self.bmi in range(20, 25):
                print("Nice body, so good!!!")
            if self.bmi in range(25, 31):
                print("little overweight, attention your diet!!")
            if self.bmi > 30:
                print("omg, you are a pig!!!, Pls eat less", self.bmi > 30)
        else:
            if self.bmi < 18:
                print("too thinnnnnn, Pls eat!!!!")
            if self.bmi in range(18, 23):
                print("Nice body, so good!!!")
            if self.bmi in range(23, 30):
                print("little overweight, attention your diet!!")
            if self.bmi > 30:
                print("omg, you are a pig!!!, Pls eat less", self.bmi > 30)
b8 = BMI()
b8.body_mass_index()
b8.bmi_information()