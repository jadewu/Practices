# 409. Longest Palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        l = []
        for c in s:
            if c not in l:
                l.append(c)
            else:
                l.remove(c)
        # len(hash) is the number of the odd letters
        if len(l) > 0:
            return len(s) - len(l)
        else return len(s)
