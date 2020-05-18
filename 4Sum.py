# 求出nums中两两之和s，新的t=target-s，对剩下来的数做2Sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = {}
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                s = nums[i] + nums[j]
                if s in d:
                    d[s].append([i, j])
                else:
                    d[s] = [[i, j]]
        res = set()
        print(d)
        for n, s in d.items():
            t = target - n
            
            for k in s:
                dic = {}
                if k[1] == len(nums)-1:
                    continue
                for m in range(k[1]+1, len(nums)):
                    if t-nums[m] in dic:
                        res.add((nums[k[0]], nums[k[1]], t-nums[m], nums[m]))
                    else:
                        dic[nums[m]] = 1
        return res
