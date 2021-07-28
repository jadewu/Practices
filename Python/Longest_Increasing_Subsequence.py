# DP + Binary Search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        res = 0
        for num in nums:
            i, j = 0, res
            while i < j:
                mid = (i+j) //2
                if dp[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            dp[i] = num
            # print(dp)
            res = max(i+1, res)
        return res

# 普通DP，每个点找到它之前的dp[j]最大且比它数值小的点，dp[i] = max(dp[j]) + 1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        res = 0
        for i in range(len(nums)):
            maxval = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxval = max(maxval, dp[j])
                    # print(maxval)
            dp[i] += maxval + 1
            res = max(res, dp[i])
        return res
