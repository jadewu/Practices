# DP解法，O(mn)
# 在每个点建立三个参数：最左，最右，高度
# 高度是这一列的这一点处累计连续高度
# 最左和最右通过比较上一列的left, right值和cur_left, cur_right大小，选择记录
# 从左开始遍历一行，如果遇到0，cur_left移到0的右边，记录0，保证在之后的比较中不会被选到
# 如果是1，需要比较上一行储存的left值和这一行的cur_left，选较大的做记录
# 从右开始遍历一行，如果遇到0，cur_right移到0的左边，记录n，保证在之后的比较中不会被选到
# 如果是1，需要比较上一行储存的right值和这一行的cur_right，选较小的做记录
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        # 每一个位置都有三个参数，最左、最右、高度
        left = [0] * n
        right = [n] * n
        height = [0] * n
        res = 0
        # 遍历每一行，计算这一行的每个位置对应的面积，然后求出最大
        for i in range(m):
            # update height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                     height[j] = 0
            # print("H ", height)
            # update left
            cur_left = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(cur_left, left[j])
                else:
                    left[j] = 0
                    cur_left = j + 1
            # print("L ", left)
            # update right
            cur_right = n
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # print("R ", right)
            for j in range(n):
                res = max(res, height[j]*(right[j] - left[j]))
        return res

# 柱状图-stack解法，O(mn)
# 首先需要清除最大矩形的边界：左右上下边会有0
# 然后需要确定矩形的高度和宽度，高度可以通过找到每个位置对应的最长连续1的值来定
# 比如：
# 0 1 1 1 0
# 0 0 1 1 1
# 1 1 1 1 0
# 第一行的heights：
# 0 1 1 1 0
# 第二行的heights:
# 0 0 2 2 1
# 第三行的heights：
# 1 1 3 3 0
# 每到新的一行就重新计算一次每个位置对应的最大矩形面积，通过这一行的heights值
# 第一行计算面积：
# 0 1 2 3 0
# 第二行计算面积：
# 0 0 2 4 1
# 第三行计算面积：
# 1 2 3 6 0
# 在第三行第四列的位置，有两个可以选择的最大面积：4 * 1 或 3 * 2，用max()解决
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        if matrix == [[]]:
            return 0
        n = len(matrix[0]) # 每一行的长度
        height = [0] * (n+1) # 高度的stack
        ans = 0
        for row in matrix:
            for i in range(n):
                # 获取每一列对应的height值
                if row[i] == '1':
                    # 不同row的相同列i，如果是1，就增加height
                    height[i] = height[i] + 1 
                else:
                    height[i] = 0 # 是0的话，停止，之后需要重新计算
            stack = [-1] # 单调stack
            # 在更新完这一行对应的height值之后，先进行面积的更新，再进入下一行的计算
            # 找到这一行中的最大面积
            for i in range(n+1):
                while height[i] < height[stack[-1]]:
                    # 当碰到比现有的最大项小，更新面积，pop()是移除list的最后一项
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1] # 连续的 
                    ans = max(ans, h*w)
                stack.append(i)
        return ans
