"""Bài 07: Viết hàm
        def create_matrix(n, m)
    xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j"""
def create_matrix(n, m):
    a = [[i * j for j in range(1, m+1)] for i in range(1, n+1)]
    for hang in a:
        print(' '.join([str(phan_tu)for phan_tu in hang]))     #join: nỗi chuỗi các phần tử trong hàng
print(create_matrix(4,5))