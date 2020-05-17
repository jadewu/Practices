# 5/16 - 1题 - #15.3Sum  
# 先sort nums，对nums里的前len-1个数进行2sum的操作，target=0-num[i]，
# 然后把target和nums[i+1:]代入2sum求出。
# 为了避免重复，nums里相同的数只进行一次操作，nums里最后两项不用进行操作，操作时输入的数列是从i+1项开始的，
# 最后放进set()里排除重复list，复杂度O(n^2)，
# 问题是，如果是用一个单独的for loop来做最后的排重，就会超时orz

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            if i>=1 and nums[i] == nums[i-1]:
                continue
            t = 0 - nums[i]
            d = {}
            for j in range(i+1, len(nums)):
                if t - nums[j] in d:
                    res.add((nums[i], nums[j], t-nums[j]))
                else:
                    d[nums[j]] = 1
        res = map(list, res)
        return res
