# 最开始的想法
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        m = []
        for i in s.lower():
            if (i>='a' and i<='z') or (i >= '0' and i <= '9'):
                l.insert(0,i)
                m.append(i)

        if l == m:
            return True
        return False

# 可以用filter选出alphanumeric，然后用[::-1]得出reversed list 
  class Solution:
    def isPalindrome(self, s: str) -> bool:      
        alpha_filter = filter(str.isalnum,s)
        ste = "".join(alpha_filter)
        ste1=ste[::-1]
        if ste.lower()==ste1.lower():
            return True
        return False
