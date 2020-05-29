# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
# 这道题必须要binary search做，不然会超时
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i <= j:
            mid = (i+j)//2
            #print(mid)
            if isBadVersion(mid):
                j = mid - 1
            else:
                i = mid + 1
        return i
