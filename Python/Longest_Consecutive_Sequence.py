# Hashset, O(n)
# 遍历list，遇到数i，判断i-1是否在set里
# 如果不在，那把i作为起点，算连续数列；如果在，就说明这个连续数列已经被算过了
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 0
        
        for num in nset:
            if num-1 not in nset:
                cur = num
                cl = 1
                while cur+1 in nset:
                    cur += 1
                    cl += 1
                res = max(res, cl)
        
        return res
