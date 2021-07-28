# 直接遍历 O(n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if target in m:
                return True
        return False

# 当成一个list看，二分查找 O(logm + logn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        if matrix == [[]]:
            return False
        row, col = len(matrix), len(matrix[0])
        i, j = 0, row*col-1
        while i <= j:
            mid = (i+j)//2
            if target < matrix[mid//col][mid%col]:
                j = mid - 1
            elif target > matrix[mid//col][mid%col]:
                i = mid + 1
            else:
                return True
        return False

# 两次二分查找，先求出row，再判断是否在row里 O(logm + logn)        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        if matrix == [[]]:
            return False
        i, j = 0, len(matrix)-1
        while i <= j:
            mid = (i+j)//2
            if target < matrix[mid][0]:
                j = mid - 1
            elif target > matrix[mid][0]:
                i = mid + 1
            else:
                return True
        row = j
        i, j = 0, len(matrix[0])-1
        while i <= j:
            mid = (i+j)//2
            if target < matrix[row][mid]:
                j = mid - 1
            elif target > matrix[row][mid]:
                i = mid + 1
            else:
                return True
        return False    
