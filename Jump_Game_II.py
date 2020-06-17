# Greedy, 遍历第一项到倒数第二项，计算能到达的最远的位置
# 如果从这点出发能到的最远位置比之前的最远位置要远，就更新，否则保持不变
# last记录的是之前计算出的最远位置，如果遍历到这里，就记一次跳跃，把新的最远位置记到last里
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cur, last = 0, 0
        times = 0
        for i in range(n-1):
            cur = max(cur, i+nums[i])
            if i == last:
                last = cur
                times += 1
        return times
        
# 同样是greedy，不过用一个pointer表示当前位置，另一个pointer计算能走的最远位置
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, nums[0]
        times = 1
        if len(nums) == 1:
            return 0
        while r < len(nums)-1:
            times += 1
            nxt = 0
            for i in range(l,r+1):
                nxt = max(i+nums[i],nxt)
            l, r = r, nxt

        return times

# 这个方法是对的，但是最后一个case超时了，大概是O(n^2)，逐个比较
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        for i in range(n-2, -1, -1):
            if nums[i] >= n-i:
                dp[i] = 1
                continue
            dp[i] = n
            for j in range(i+1, i+nums[i]+1):
                dp[i] = min(dp[j]+1, dp[i])
        return dp[0]
