# 简洁
class Solution:
    def isUgly(self, num: int) -> bool:
        for i in (2, 3, 5):
            while num % i == 0 and num > 0:
                num = num / i
        if num == 1:
            return True
        return False

# recursion
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        if num % 2 == 0:
            return self.isUgly(num/2)
        elif num % 3 == 0:
            return self.isUgly(num/3)
        elif num % 5 == 0:
            return self.isUgly(num/5)
        else:
            return False
