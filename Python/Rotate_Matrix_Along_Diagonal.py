# 顺时针沿对角线旋转矩阵
# 两条对角线上的数不动，其他的swap
matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
'''
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''
k = 2
n = len(matrix)
while k:
    for i in range(n//2):
        for j in range(i+1, n-1-i):
            matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
    k -= 1
print(matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[3])
print(matrix[4])
