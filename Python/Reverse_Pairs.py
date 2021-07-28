# 比较直观的方法，维护一个排序好的visited数列，用binary search做查找和插入能把复杂度降到nlogn
class Solution:
  #牢牢记住二分法的写法，往左移的时候要把mid包括进去
    def bs(self, nums, tar):
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j)//2
            if tar <= nums[mid]:
                j = mid
            else:
                i = mid+1
        return i
                
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) in (0,1):
            return 0
        visited = [nums[0]]
        res = 0
        for n in range(1, len(nums)):
            nidx = self.bs(visited, nums[n]+1)
            tnidx = self.bs(visited, 2*nums[n]+1)
            # print(nidx, tnidx)
            if visited[-1] > 2*nums[n]:
                res += len(visited)-tnidx
            if visited[-1] < nums[n]:
                visited.append(nums[n])
            else:
                visited.insert(nidx, nums[n])
            # print(visited)
        return res
            
