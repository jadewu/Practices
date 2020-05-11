class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # input: 1,2,5,4,3,2 result: 1,3,2,2,4,5
        # change 2 with 3: 1,3,5,4,2,2
        # reverse the nums after 3: 1,3,2,2,4,5

        n = len(nums)
        i = j = n - 1
        # find the left most number in ascending order, i-1
        while i > 0 and nums[i-1] >= nums[i]:
            i = i - 1
            
        # the whole list is in descending order, so just reverse all
        if i == 0:
            nums.reverse()
            return # stop here
        
        # find the left most number > i-1, and swap them two
        while nums[j] <= nums[i-1]:
            j = j - 1
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # reverse the remaining part
        k = n - 1
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i = i + 1
            k = k - 1
