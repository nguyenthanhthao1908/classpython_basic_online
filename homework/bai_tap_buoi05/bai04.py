L = [(2, 4, 7), (1, 2), (55, 6, 99)]
#sử dụng lambdag để gán biến i, dùng sorted mặc định sx tăng
print(sorted(L, key=lambda i: float(i[-1])))