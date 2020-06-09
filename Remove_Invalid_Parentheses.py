# BFS 每次循环去掉任意一个字符，把所有情况存入下次循环的list里
# 判断list里的字符串是否有valid，如果有，直接输出
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(s):
            a = 0
            for c in s:
                if c == '(':
                    a += 1
                elif c == ')':
                    if a == 0:
                        return False
                    else:
                        a -= 1
            if a == 0:
                return True
            return False
        cur = [s]
        # BFS
        while True:
            res = []
            # 判断在cur的所有字符串中，有没有valid的结果
            # 如果有valid结果，放入res
            for e in cur:
                if valid(e):
                    res.append(e)
            # 因为是minimum # of removes，每次增加一次改动
            # 所以只要有valid结果了，就直接输出
            if res:
                return res
            # 还没有出现valid结果，继续做remove
            new = []
            # 对于cur里的每一个字符串，减去一个字符得到的新的字符串都存进new里面
            # 得到的new就包括比cur短一个字符的所有可能的字符串
            for e in cur:
                for i in range(len(e)):
                    new.append(e[:i] + e[i+1:])
            cur = list(set(new))
