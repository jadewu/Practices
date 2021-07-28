# 不需要操作！！！
# 直接一遍遍历搞定！数据很大！！
# 其实就是要找最大值
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        curmax = arr[0]
        d = {}
        for a in arr:
            d[a] = 0
        for i in range(1, len(arr)):
            if arr[i] >= curmax:
                curmax = arr[i]

            d[curmax] += 1
            if d[curmax] == k:
                return curmax
        return curmax
