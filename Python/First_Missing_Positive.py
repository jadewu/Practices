# 用sort的方法，O(nlogn)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        last = 1
        for i in range(n):
            if nums[i] == last:
                last += 1
            elif nums[i] > last:
                return last
        return last

# 答案，O(n)
# 遍历第一遍，把nums里面小于等于0和大于n的项都改为1
# 遍历第二遍，把第abs(nums[i])项的符号变为负，用来表示正整数abs(nums[i])已经出现了，如果nums[i]==n，就把第0项变为负
# 遍历第三遍，从1到n-1，找到第一个符号不为负的数，是第i项，那么表示正整数i并未在数列里出现过
# 如果1到n-1项都为负且第0项为正，那么最小正整数是n
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # nums = [1]
        if n == 1:
            return 2
        
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain 
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # Now the index of the first positive number 
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
            
        return n + 1
