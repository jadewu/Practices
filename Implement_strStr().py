# 逐个比较
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            flag = 1
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    flag = 0
                    break
            if flag:
                return i
        return -1
# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
