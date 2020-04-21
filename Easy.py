# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i=='(' or i=='[' or i=='{':
                l.append(i)
            else:
                if not len(l):
                    return False
                u = l.pop(-1)
                if (i==')' and u=='(') or (i==']' and u=='[') or (i=='}' and u=='{'):
                    continue
                else:
                    return False
        if len(l):
            return False
        else:
            return True
