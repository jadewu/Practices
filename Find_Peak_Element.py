# log n 的复杂度
# 二分查找：binary search
# 无限右移，因为假设的是nums[n]是负无穷
# 所以如果是ascending的，最右一定是peak
# 如果不是ascending，那就在中间会有peak或者没有peak
# Iterative solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
# Recursive solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def binsearch(nums, l, r):
            if l == r:
                return l
            mid = (l+r)//2
            if nums[mid]<nums[mid+1]:
                return binsearch(nums,mid+1,r)
            else:
                return binsearch(nums,l,mid)
        return binsearch(nums,0,len(nums)-1)
