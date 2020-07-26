# 两次binary search，分别找到first和last
# 一定要是left<=right，每次二分，移到mid + 1或mid - 1的位置
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
#         开头不可以这样写，因为in/ not in相当于是做了一遍遍历，O(n)
#         if target not in nums:
#             return [-1, -1]
        i, j = 0, len(nums)-1
        res = [-1, -1]
        if nums == []:
            return [-1, -1]
        while i <= j:
            mid = (i+j) //2
            if nums[mid] >= target:
                j = mid - 1
            else:
                i = mid + 1
        if (0 <= i <= len(nums)-1) and (nums[i] == target): 
            res[0] = i
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i+j) //2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid - 1
        if (0 <= j <= len(nums)-1) and (nums[j] == target):
            res[1] = j
        return res  
