# 比较简洁的做法：从后往前merge，将m、n作为pivot，最后copy nums2前面多出来的部分
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
        if n > 0:
            nums1[:n] = nums2[:n]
# 第一次想到的做法，从前往后，比较->插入->补上末尾
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = 0
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return

        for i in range(m+n):
            if p < n:
                if nums1[i] > nums2[p]:
                    nums1.insert(i, nums2[p])
                    nums1.pop()
                    p += 1 
                if i >= m + p:
                    nums1[i] = nums2[p]
                    p += 1
