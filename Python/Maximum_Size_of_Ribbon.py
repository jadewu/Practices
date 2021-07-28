# 剪绳子，给一些不同长度的绳子，至少要得到k段相同长度的段，求可以得到的最长段长度
# 比如段长是3，对于这些绳子，1、2无法得到，3、4、9分别可以得到1、1、3段，所以可以得到5段长度为3的分段，满足条件
# 用一个另外的函数来判断是否能得到至少k段，用二分法来找到最长段
ribbon = [1, 2, 3, 4, 9]
k = 5
def check(arr, size, k):
    ct = 0
    for r in arr:
        ct += r//size
    if ct >= k:
        return True
    return False
i, j = 1, max(ribbon)
while i+1 < j:
    mid = (i+j)//2
    if check(ribbon, mid, k):
        i = mid
    else:
        j = mid - 1
if check(ribbon, j, k):
    print(j)
elif check(ribbon, i, k):
    print(i)
else:
    print(0)
