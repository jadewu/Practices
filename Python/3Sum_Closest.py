# 两个for loop确定前两个，最后一个通过bisect函数找到nums里最接近target的，会比再用一个for loop遍历要快一些
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        dis = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                com = target - nums[i] - nums[j]
                # 找到nums里从j+1开始往右，最接近com且大于或等于它的
                hi = bisect_right(nums, com, j+1)
                # 这是最接近com且比它小
                lo = hi - 1
                if hi < len(nums) and abs(com - nums[hi]) < abs(dis):
                    dis = com - nums[hi]
                if lo > j and abs(com - nums[lo]) < abs(dis):
                    dis = com - nums[lo]
            if dis == 0:
                break
        return target - dis

# 三个for loop直接搜索的方法，复杂度超了
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sums = []
        dis = float('inf')
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    s = nums[i]+nums[j]+nums[k]
                    if abs(s - target) < dis:
                        res = s
                        dis = abs(s-target)
                    # print(dis, res)
        return res
