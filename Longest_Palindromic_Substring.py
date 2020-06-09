# DP解法，建立一个2d matrix，初始设为0
# 从后往前判断dp[i
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    if res == "" or longest < j-i+1:
                        res = s[i:j+1]
                        longest = j-i+1
        return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def search(s,l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        for i in range(len(s)):
            tmp = search(s,i,i)
            if len(tmp) > len(res):
                res = tmp
            tmp = search(s,i,i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
 
