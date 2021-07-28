# 找一个number array里间隔相等的最长子数列
# [3,6,9,12] 最长是整个array，4
# [9,4,7,2,10] 最长是[4,7,10]，3
# DP，用一个dp来存放数对key (i, dist)，i是间隔相等子数列的起始点，dist是间隔长度，value是满足条件的子数列长度
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(1, len(A)):
            for j in range(i):
                dist = A[i] - A[j]
                if (j, dist) in dp:
                    dp[i, dist] = dp[j, dist] + 1
                else:
                    dp[i, dist] = 2
        return max(dp.values())

# 变型：两个数列A、B，可以把B里的元素插入到A里，使得A成为一个间隔相等的数列，求能得到的最长A
