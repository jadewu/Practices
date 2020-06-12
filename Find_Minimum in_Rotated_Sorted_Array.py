# The list is in ascending order but moving left part to the front like (4,5,1,2,3)
# Binary search is efficient in finding an element in sorted list
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        # nums.sort()
        return nums[l]
