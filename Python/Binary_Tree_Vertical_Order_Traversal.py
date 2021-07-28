# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 为什么要用BFS？
# 因为垂直遍历要求的顺序是从上到下+从左到右，为了满足从左到右，用BFS最好
# 在遍历的过程中，记下每个node对于root的相对位置，[...-2, -1, 0, 1, 2...]，相同数字的放在一起（dict）
# 最后能按照相对位置数字从小到大归类
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        columns = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            current = queue.pop(0)
            node, col = current[0], current[1]
            columns[col].append(node.val)
            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col+1))
        res = []
        for col, nodes in sorted(columns.items()):
            nl = []
            for node in nodes:
                nl.append(node)
            res.append(nl)
        return res
