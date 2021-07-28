# DP, value of (row, col) = value of (row-1, col-1) + value of (row-1, col)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for num in range(numRows):
            row = [None for _ in range(num+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row)-1):
                row[j] = triangle[num-1][j-1] + triangle[num-1][j]
            triangle.append(row)
        return triangle
