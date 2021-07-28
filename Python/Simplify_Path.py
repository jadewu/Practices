# 简单处理一下字符串
class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        res = ""
        i = 0
        d = []
        for i in l:
            if (i != '') and (i != '.'):
                if i == '..':
                    if d:
                        d.pop()
                else:
                    d.append(i)
        for j in d:
            res += "/" + j
        if (not d) and path:
            res = "/"
        return res
