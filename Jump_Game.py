# Greedy, (其实我也不知道为什么是greedy)，O(n)
# 如果这个点可以到goal，新goal=这个点；如果这个点不能到goal，那goal还是原来的位子
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return not goal
