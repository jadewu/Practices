"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# Recursive DFS解法
# serialize的输出是：1 3 5 # 6 # # 2 # 4 # #
# 每次返回上一层就会打一个#来分隔，1->3->5; 3->6; 1->2; 1->4
# deserialize的时候用#来判断是否要循环
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serial = []
        
        def dfs(node):
            if not node:
                return
            serial.append(str(node.val))
            for child in node.children:
                dfs(child)
            serial.append("#")      

        dfs(root)
        return " ".join(serial)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        nodes = data.split()
        root = Node(int(nodes.pop(0)), [])

        def recover(parent):
            if not nodes:
                return
            while nodes[0] != "#": # add child nodes with subtrees
            # 如果不是#，就表示dfs还没有到头，继续往下加子节点
                child = Node(int(nodes.pop(0)), [])
                parent.children.append(child)
                recover(child)
            # 如果是#，就表示返回上层，直接pop就行
            nodes.pop(0)        # discard the "#"

        recover(root)
        return root   
        
# Iterative BFS解法，自己的做法
# serialize的输出是：1 ,3 2 4 #,5 6 ###,##,
# 空格用来分开数字，逗号用来分行，#用来分开子节点和表示null
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res = ""
        level = [root]
        while level:
            new_level = []
            for node in level:
                if not node:
                    res += "#"
                    continue
                else:
                    res += str(node.val) + " "
                if node.children:
                    for c in node.children:
                        new_level.append(c)
                new_level.append(None)
            level = new_level
            res += ","
        # print(res)
        return res
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        levels = data.split(",")
        if levels[0] == '#':
            return None
        root = Node(int(levels[0].split()[0]), [])
        parents = [root]
        # print(levels)
        for i in range(1,len(levels)):
            level = levels[i].split("#")
            # print(level)
            new_parents = []
            for p in range(len(parents)):
                if p > len(level)-1 or (not level[p]):
                    # print(parents[p].val, "Jump")
                    continue
                children = level[p].split()
                # print(parents[p].val, children)
                for c in children:
                    child = Node(int(c), [])
                    parents[p].children.append(child)
                    new_parents.append(child)
            parents = new_parents
        return root     

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
