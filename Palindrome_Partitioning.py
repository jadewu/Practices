# 典型的backtracking
# 需要注意的是，这种求所有路径的题，写backtracking的时候，需要把path和res作为两个parameters
# s == ""的时候，把path加到res里
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(s, path, res):
            if s == "":
                npath = []
                for n in path:
                    npath.append(n)
                res.append(npath)
                return res
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    path.append(s[:i])
                    # print(s, path)
                    res = backtrack(s[i:], path, res)
                    path.pop()
            return res
        return backtrack(s, [], [])
