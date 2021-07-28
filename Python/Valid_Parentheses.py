# 注意一些边界情况，多写test cases：s = "", s = "(", s = ")", s = "}("...
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ('(','[','{'):
                stack.append(i)
            elif not stack:
                return False
            elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False
