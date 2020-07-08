class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s, left, right):
            if len(s) == 2*n:
                res.append(s)
                return
            # start a new bracket
            if left < n:
                backtrack(s+"(", left+1, right)
            # or end the inner most one
            if right < left:
                backtrack(s+")", left, right+1)
        backtrack("", 0, 0)
        return res
