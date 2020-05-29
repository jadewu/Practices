# 因为对于每一行每一列从上到下，从左到右都是asc的，从[0][n-1]开始寻找，大了就左移，小了就下移
# O(m + n)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        if matrix == [[]]:
            return False
        i, j = 0, len(matrix[0])-1
        print(i,j)
        while (i<len(matrix)) and (j>=0):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
                

# 二分查找，O(mlogn)
class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == []:
            return False
        if matrix == [[]]:
            return False
        j = 0
        while j < len(matrix):
            if target < matrix[j][0]:
                j += 1
                continue
            l, r = 0, len(matrix[0])-1
            while l <= r:
                mid = (l+r)//2
                if target == matrix[j][mid]:
                    return True
                elif target < matrix[j][mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            j += 1
        return False
        
# 直接遍历 O(mn)
class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == []:
            return False
        if matrix == [[]]:
            return False
        i = 0
        while i < len(matrix):
            if target >= matrix[i][0]:
                if target in matrix[i]:
                    return True
            i += 1
        return False
